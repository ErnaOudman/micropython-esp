import dht
import machine

led = machine.Pin(16, machine.Pin.OUT)

d = dht.DHT11(machine.Pin(14))
d.measure()
d.temperature()