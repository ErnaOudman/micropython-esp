import socket
import machine
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('', '')
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
LED_BLUE = machine.Pin(14, machine.Pin.OUT)


#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ipadr, 80))
s.listen(5)
while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    # raise ValueError(request)
    request = str(request)
    LEDON_BLUE = request.find('/?LED=ON_BLUE')
    LEDOFF_BLUE = request.find('/?LED=OFF_BLUE')


    # LEDON_BLUE = request.GET('LED') == ON_BLUE
    # LEDOFF_BLUE = request.GET('LED') == OFF_BLUE

    print('LEDon: {}, LEDoff {}'.format(LEDON_BLUE, LEDOFF_BLUE))

    if LEDON_BLUE == 293:
        print('TURN LED2 ON')
        LED_BLUE.value(0)
    if LEDOFF_BLUE == 293:
        print('TURN LED2 OFF')
        LED_BLUE.value(1)     
    response = html
    conn.send(response)
    conn.close()