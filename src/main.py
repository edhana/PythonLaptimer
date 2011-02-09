import SER
import GPS
import MOD

SPEED_LOWER_LIMIT=5 # Minimum speed limit to save gps data
GPS_LOG_FILE_NAME="input.log"
    
def write_on_file(file, gps_data):
    pass
    
def is_valid_message(gps_split_message):
    # verify the fixmode at the 6th element of array
    if (int(gps_split_message[5]) == 3):
        return 1
    else:
        return 0
    
def get_formated_gps_data():
    gps_string = GPS.getActualPosition()
    
    gps_split_message = gps_string.split(',')
    
    return_message = ""
    
    if is_valid_message(gps_split_message):
        return_message = "%s,%s,%s,%s,%s,%s,%s"%(gps_split_message[0], gps_split_message[1], gps_split_message[2], 
            gps_split_message[4], gps_split_message[5],gps_split_message[6], gps_split_message[7])
    
    return  return_message

'''
    Basic loop function of this app.
'''
def loop(gps_log_file):
    gps_data = get_formated_gps_data()
    
    if gps_log_file != None and gps_data != None and gps_data != "":
        #SER.send("Gravou: %s --- TEMPO: %d\n"%(gps_data, MOD.secCounter()))
        gps_log_file.write("%s\n"%gps_data)
        gps_log_file.flush()
    
    
if __name__ == "__main__":
    SER.set_speed("115200")
    SER.send("Iniciando cliente Lap Timer")
    
    # Open de log file
    gps_log_file = None
    
    try:    
        gps_log_file = open(GPS_LOG_FILE_NAME, 'w')    
    except Exception, err:
        SER.send("Nao foi possivel abrir o arquivo de log: %s\n"%err)
    
    try: 
        start_time = MOD.secCounter()
        timeout = start_time+10000
        while(MOD.secCounter < timeout):
            loop(gps_log_file)
    except Exception, err2:
        SER.send("Erro na escrita do arquivo de log: %s\n"%err2)
    
    # Dont forget to close the log file
    gps_log_file.close()
    
    SER.send("FIM\n")
