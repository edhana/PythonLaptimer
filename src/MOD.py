# Mock forjado do modulo MOD da placa Telit

watchdog_enabled = False # Para usar no watchdog -- testes
watchdog_reset_times = 0 # Numero de vezes que o reset foi chamado

def secCounter():
    #print "Usando o secCounter()"
    return 0

def sleep(sec_time):
    #time.sleep(sec_time)
    #print "sleep() por %d segundos"%sec_time
    pass


def watchdogEnable(timeout):
    global watchdog_enabled
    watchdog_enabled = True
    
def watchdogReset():
    global watchdog_reset_times
    watchdog_reset_times += 1
    
