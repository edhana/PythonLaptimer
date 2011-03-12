##############################################
# This module control the at command interface
#
##############################################

import SER
import MDM
import MOD

def println(message):
    SER.send("%s\n"%message)
    
def send_at_command(command, timeout=10, response_timeout=10):
    println("sending %s..."%command)
    cmd_with_return = command + '\r'
    
    result = MDM.send(cmd_with_return, timeout)

    if result == -1:
        println('ERROR TO SEND COMMAND: ')

    response = get_response(response_timeout)
    println(response)

    return response

def get_response(timeout=10):
    response = ''

    if timeout >= 20:
        local_timeout = MOD.secCounter() + timeout
        response = MDM.read()
        while((len(response)==0) and (MOD.secCounter() < local_timeout)):
            response = response + MDM.read()
    else:
        response = MDM.receive(timeout)

    return response