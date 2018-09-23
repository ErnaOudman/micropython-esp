
import network
import machine
import time

import ssd1306
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)


def connect():

    ssid = "Thijs"
    password = "qwerasdf"

    wlan = network.WLAN(network.STA_IF)

    if wlan.isconnected() == True:
        print("Already connected")
        displayIp(wlan)
        return

    wlan.active(True)
    wlan.connect(ssid, password)

    while wlan.isconnected() == False:
        print('not connected')
        time.sleep(1)
        pass

    print("Connection successful")
    print(wlan.ifconfig())
    displayIp(wlan)


def displayIp(wlan):
    oled.fill(0)
    for idx, ip in enumerate(wlan.ifconfig()):
        print(ip)
        oled.text(str(ip), 0, 8*idx)
    oled.show()
