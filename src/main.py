import SER
import GPS
import MOD
import MDM

SPEED_LOWER_LIMIT=5 # Minimum speed limit to save gps data
GPS_LOG_FILE_NAME="input.log"

# def get_at_response(self, timeout=10):
#     response = ''
# 
#     if timeout >= 20:
#         local_timeout = MOD.secCounter() + timeout
#         response = MDM.read()
#         while((len(response)==0) and (MOD.secCounter() < local_timeout)):
#             response = response + MDM.read()
#     else:
#         response = MDM.receive(timeout)
# 
#     return response
#     
# def send_at_command(self, command, timeout=10, response_timeout=10):
#     SER.send('sending ' + command + ' ...\n')
#     cmd_with_return = command + '\r'
#     result = MDM.send(cmd_with_return, timeout)
# 
#     if result == -1:
#         SER.send('ERROR TO SEND COMMAND: %s\n'%command)
# 
#     response = get_response(response_timeout)
#     SER.send("%s\n"%response)
# 
#     return response
    
def is_valid_message(gps_split_message):
    # verify the fixmode at the 6th element of array TODO: Verify the speed to
    if (int(gps_split_message[5]) == 3):
        return 1
    else:
        return 0
    
def get_formated_gps_data():
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
        # return_message = "%s,%s,%s,%s,%s,%s,%s"%(gps_split_message[0], gps_split_message[1], gps_split_message[2], 
        return_message = "%s,%s,%s,%s,%s,%s"%(gps_split_message[0], gps_split_message[1], gps_split_message[2], gps_split_message[5],gps_split_message[6], gps_split_message[7])
        
    return  return_message
    
def get_speed(gps_data):
    return int(gps_split_message[7])

'''
    Basic loop function of this app.
'''
def loop(gps_log_file):
    gps_data = get_formated_gps_data()
    
    if gps_log_file != None and gps_data != None and gps_data != "":
        # if get_speed(gps_data) > 5: # if speed is greater than 5km/h
        # SER.send("Gravou: %s --- TEMPO: %d\n"%(gps_data, MOD.secCounter()))
        gps_log_file.write("%s\n"%gps_data)
        gps_log_file.flush()

    
if __name__ == "__main__":
    # TODO: Analisar se o veiculo ficou muito tempo parado. Se ficou encerrar o programa
    ACQUIRE_STARTED = 0 # Boolean
    ACQUIRE_PAUSED = 0 # Boolean
    ACQUIRE_START_TIME = 0 # Time variable
    ACQUIRE_PAUSED_TIME = 0
    
    SER.set_speed("115200")
    SER.send("Iniciando cliente Lap Timer em %d"%MOD.secCounter())
    
    # Open the log file
    gps_log_file = None
    
    # try:
    #     # Tenta iniciar a configuracao do modulo
    #     send_at_command("AT#SELINT=2")        
    # except:
    #     SER.send("Erro ao iniciar o modulo.\n")
        
    try:    
        gps_log_file = open(GPS_LOG_FILE_NAME, 'w')    
    except Exception, err:
        SER.send("Nao foi possivel abrir o arquivo de log: %s\n"%err)
    
    try: 
        start_time = MOD.secCounter()
        
        while(1):
            loop(gps_log_file)
            # enxerta uma pausa para deixar o flush rolar
            MOD.sleep(4) # Pausa por 4 decimos de segundo
            
    except Exception, err2:
        SER.send("Erro na escrita do arquivo de log: %s\n"%err2)
    
    # Dont forget to close the log file
    gps_log_file.close()
    
    SER.send("FIM\n")
