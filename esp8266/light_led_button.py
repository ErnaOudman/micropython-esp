import machine, ssd1306
import time

button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(14, machine.Pin.OUT)
i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))

oled = ssd1306.SSD1306_I2C(128, 64, i2c)
while True:
    first = button.value()
    time.sleep(0.01)
    second = button.value()
    if first and not second:
        led.on()
        oled.fill(0);oled.text('Lampje aan', 0, 0);oled.show()
    elif not first and second:
        led.off()
        oled.fill(0);oled.text('Lampje uit', 30,0);oled.show()