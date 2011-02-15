# Mock forjado do modulo MOD da placa Telit
import time

watchdog_enabled = 0 # Para usar no watchdog -- testes
watchdog_reset_times = 0 # Numero de vezes que o reset foi chamado

def secCounter():
    #print "Usando o secCounter()"
    return int(time.time())

def sleep(sec_time):
    #time.sleep(sec_time)
    #print "sleep() por %d segundos"%sec_time
    pass


def watchdogEnable(timeout):
    global watchdog_enabled
    watchdog_enabled = 1
    
def watchdogReset():
    global watchdog_reset_times
    watchdog_reset_times = watchdog_reset_times + 1
    
