import SER
import GPS
import MOD

import command

SPEED_LOWER_LIMIT=5 # Minimum speed limit to save gps data
GPS_LOG_FILE_NAME="input.log"
gps_split_message = []
    
def is_valid_message(gps_split_message):
    # verify the fixmode at the 6th element of array TODO: Verify the speed to
    if (int(gps_split_message[5]) == 3):
        return 1
    else:
        return 0
    
def get_formated_gps_data():
    global gps_split_message
        
    gps_split_message = []
    
    # Get the gps string
    gps_string = GPS.getActualPosition()
    
    gps_split_message = gps_string.split(',')
    
    return_message = ""
    
    # 0 - tempo
    # 1 - latitude
    # 2 - Longitude
    # 5 - Fix
    # 6 - Angulo 
    # 7 - Velocidade
    
    if gps_split_message != None and gps_split_message != "" and is_valid_message(gps_split_message):
        return_message = "%s,%s,%s,%s,%s,%s"%(gps_split_message[0], 
            gps_split_message[1], 
            gps_split_message[2], 
            gps_split_message[5],
            gps_split_message[6], 
            gps_split_message[7])
        
    return  return_message
    
def get_speed(gps_data):
    global gps_split_message
    
    return int(gps_split_message[7].split(".")[0])

'''
    Basic loop function of this app.
'''
def loop(gps_log_file):
    gps_data = get_formated_gps_data()
    
    if gps_log_file != None and gps_data != None and gps_data != "":
        if get_speed(gps_data) > 10: # write only if speed is greater than 10 km/h
            gps_log_file.write("%s\n"%gps_data)
            gps_log_file.flush()
        else:
            # close the log file
            gps_log_file.flush()
            gps_log_file.close()

def init():
    try:
        # Init the module configuration
        command.send_at_command("AT#SELINT=2")
        
        # Set the command mode       
        command.send_at_command("AT&K0")
        
        # Configure GPS speed
        command.send_at_command("AT$GPSS=57600")
        
    except Exception, err:
        SER.send("Erro ao iniciar o modulo: %s\n"%err)
        
def get_new_log_filename():
    # Get the gps string
    gps_string = GPS.getActualPosition()

    gps_split_message = gps_string.split(',')

    if is_valid_message(gps_split_message):
        return "laptimer%s.log"%gps_split_message[0].split('.')[0]

    return ''        
    
if __name__ == "__main__":
    SER.set_speed("115200")
    SER.send("Iniciando cliente Lap Timer em %d\n"%MOD.secCounter())
    
    # Watchdog set to 20 seconds
    MOD.watchdogEnable(20) 
    
    # Open the log file
    gps_log_file = None
    
    init()
        
    log_filename = ''
    
    while(log_filename == ''):
        log_filename = get_new_log_filename()
        if log_filename == '':
            SER.send("Nome de arquivo de log nao criado.\n")
            MOD.sleep(10)
        else:
            SER.send("Nome do novo arquivo: %s"%log_filename)
            MOD.watchdogReset()
        
    try:    
        gps_log_file = open(GPS_LOG_FILE_NAME, 'w')    
    except Exception, err:
        SER.send("Nao foi possivel abrir o arquivo de log: %s\n"%err)
    
    if gps_log_file != None:
        
        try: 
            start_time = MOD.secCounter()
        
            while(1):
                loop(gps_log_file)
                MOD.watchdogReset()
                
                # Sleep to let the file flush work
                MOD.sleep(2)
            
        except Exception, err2:
            SER.send("Erro na escrita do arquivo de log: %s\n"%err2)
    
        # Dont forget to close the log file
        gps_log_file.close()
    
    SER.send("FIM\n")
