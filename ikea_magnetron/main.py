import tm1637
from machine import Pin
import time
import network
import socket
tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))

# Rotary encoder
from rotary_irq_esp import RotaryIRQ
r = RotaryIRQ(
    pin_num_clk=14,
    pin_num_dt=12,
    min_val=0,
    max_val=200,
)

wifi = network.WLAN(network.AP_IF)
wifi.active(True)
print(wifi.ifconfig())
ipadr = wifi.ifconfig()[0]

html = "<!DOCTYPE html><html><h1>Ik doe het!</h1></html>"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ipadr, 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    request=conn.recv(1024)
    cur_val = r.value()
    # print(r.value())
    minutes = int(cur_val/60)
    seconds = cur_val%60
    # tm.numbers(minutes,seconds)
    print('minutes: {}, seconds: {}'.format(minutes,seconds))
    time.sleep(.2)
    conn.send(html)
    conn.close()
