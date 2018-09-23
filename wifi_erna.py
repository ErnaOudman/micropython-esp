import socket
import machine
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('NAME', 'PWD')
wlan.ifconfig()


ipadr = wlan.ifconfig()[0]

#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 LED ON/OFF</title> </head>
<h2>LED's on and off with Micropython</h2></center>
<h3>(ESP8266 HUZZAH Feather)</h3></center>
<form>
LED BLUE:
<button name="LED" value="ON_BLUE" type="submit">LED ON</button>
<button name="LED" value="OFF_BLUE" type="submit">LED OFF</button>
</form>
</html>
"""

#Setup PINS
LED_BLUE = machine.Pin(2, machine.Pin.OUT)


#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ipadr, 80))
s.listen(5)
while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    LEDON_BLUE = request.find('/?LED=ON_BLUE')
    LEDOFF_BLUE = request.find('/?LED=OFF_BLUE')

    if LEDON_BLUE == 6:
        print('TURN LED2 ON')
        LED_BLUE.off()
    if LEDOFF_BLUE == 6:
        print('TURN LED2 OFF')
        LED_BLUE.on()     
    response = html
    conn.send(response)
    conn.close()





import network 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.scan()

wlan.connect('Ziggo11776', '7kwaTTNtUeEa')
wlan.isconnected()

wlan.ifconfig()

from machine import Pin

pin = Pin(13, Pin.IN)

html = """<!DOCTYPE html>
<html>
    <head> <title>Pi4IoT</title> </head>
    <body> 
      <h1>ESP8266 - Pi4IoT</h1>
        <table border="1" bgcolor="#909090"> 
            <tr>
                <th>Pin</th><th>Value</th>
            </tr> %s 
        </table>
    </body>
</html>
"""

import socket
ipadr = wlan.ifconfig()[0]
addr = socket.getaddrinfo(ipadr, 80)[0][-1]


# Turn LED on/off
import socket
import machine
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Ziggo11776', '7kwaTTNtUeEa')
wlan.ifconfig()


ipadr = wlan.ifconfig()[0]
# addr = socket.getaddrinfo(ipadr, 80)[0][-1]

#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 LED ON/OFF</title> </head>
<h2>LED's on and off with Micropython</h2></center>
<h3>(ESP8266 HUZZAH Feather)</h3></center>
<form>
LED BOARD&nbsp;&nbsp;:
<button name="LED" value="ON_BOARD" type="submit">LED ON</button>
<button name="LED" value="OFF_BOARD" type="submit">LED OFF</button><br><br>
LED RED&nbsp;&nbsp;:
<button name="LED" value="ON_RED" type="submit">LED ON</button>
<button name="LED" value="OFF_RED" type="submit">LED OFF</button><br><br>
LED BLUE:
<button name="LED" value="ON_BLUE" type="submit">LED ON</button>
<button name="LED" value="OFF_BLUE" type="submit">LED OFF</button><br><br>
LED Extern:
<button name="LED" value="ON_EX" type="submit">LED ON</button>
<button name="LED" value="OFF_EX" type="submit">LED OFF</button>
</form>
</html>
"""

#Setup PINS
LED_BOARD = machine.Pin(13, machine.Pin.OUT)
LED_RED = machine.Pin(0, machine.Pin.OUT)
LED_BLUE = machine.Pin(2, machine.Pin.OUT)
# LED_EX = machine.Pin(12, machine.Pin.OUT)

#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ipadr, 80))
s.listen(5)
while True:

    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    LEDON_BOARD = request.find('/LED=ON_BOARD')
    LEDOFF_BOARD = request.find('/LED=OFF_BOARD')
    LEDON_RED = request.find('/?LED=ON_RED')
    LEDOFF_RED = request.find('/?LED=OFF_RED')
    LEDON_BLUE = request.find('/?LED=ON_BLUE')
    LEDOFF_BLUE = request.find('/?LED=OFF_BLUE')
    # LEDON_EX = request.find('/?LED=ON_EX')
    # LEDOFF_EX = request.find('/?LED=OFF_EX')    

    if LEDON_BOARD == 6:
        print('TURN LED ON')
        LED_BOARD.off()
    if LEDOFF_BOARD == 6:
        print('TURN LED OFF')
        LED_BOARD.on()
    


    if LEDON_RED == 6:
        print('TURN LED0 ON')
        LED_RED.off()
    if LEDOFF_RED == 6:
        print('TURN LED0 OFF')
        LED_RED.on()
    if LEDON_BLUE == 6:
        print('TURN LED2 ON')
        LED_BLUE.off()
    if LEDOFF_BLUE == 6:
        print('TURN LED2 OFF')
        LED_BLUE.on()
    # if LEDON_EX == 6:
    #     print('TURN LED2 ON')
    #     LED_EX.on()
    # if LEDOFF_EX == 6:
    #     print('TURN LED2 OFF')
    #     LED_EX.off()        
    response = html
    conn.send(response)
    conn.close()