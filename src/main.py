import SER
import GPS

SPEED_LOWER_LIMIT=5 # 5km de limite minimo para registrar

def open_log_file():
    pass
    
def close_log_file():
    pass
    
def write_on_file(file, gps_data):
    pass
    
def get_formated_gps_data():
    GPS.getActualPosition()

if __name__ == "__main__":
    SER.set_speed("115200")
    SER.send("Iniciando cliente Lap Timer")
    
    # Abre o arquivo onde serão colocados as coordenadas
    open_log_file()