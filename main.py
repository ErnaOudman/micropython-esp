import time, machine, onewire, ds18x20, ssd1306

# the device is on GPIO12
data = machine.Pin(12)
led = machine.Pin(2, machine.Pin.OUT)
i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# create the onewire object
ds = ds18x20.DS18X20(onewire.OneWire(data))
ds.ow.reset()
# Scan le bus OneWire et recupere l'ID de chaque sonde | scan for devices on the bus
roms = ds.scan()
print('found probes:', roms)

def get_temps():
    print('temperatures:', end=' ')
    ds.convert_temp()
    time.sleep_ms(1000)
    temps = []
    for rom in roms:
        temp = ds.read_temp(rom)
        temps.append(temp)
        print(temp, end=' ')
        oled.fill(0)
        oled.text('Temperature:',0,0)
        oled.text(str(temp), 0, 40)
        oled.show()
    return temps

temps = get_temps()

# Bouble infinie qui lit et affiche la température de chaque sonde | Infinite loop than read and print temperature of each probe
while True:
    try:
        temps = get_temps()
        if max(temps) > 28:
            led.off()
        else:
            led.on()
    except Exception:
        ds.ow.reset()
        time.sleep_ms(1000)

    print()