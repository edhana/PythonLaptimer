import SER
import GPS

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
    
    return  return_message# TODO: Implementar

'''
    Basic loop function of this app.
'''
def loop():
    # Open de log file
    gps_log_file = None
    
    gps_log_file = open(GPS_LOG_FILE_NAME, 'w')
    
    # Dont forget to close the log file
    gps_log_file.close()
    
if __name__ == "__main__":
    SER.set_speed("115200")
    SER.send("Iniciando cliente Lap Timer")
    
    while(1):
        loop()
