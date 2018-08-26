import time, machine, onewire, ds18x20

# the device is on GPIO12
data = machine.Pin(12)
led = machine.Pin(2, machine.Pin.OUT)


# create the onewire object
ds = ds18x20.DS18X20(onewire.OneWire(data))
ds.ow.reset()
# Scan le bus OneWire et recupere l'ID de chaque sonde | scan for devices on the bus
roms = ds.scan()
print('found probes:', roms)

# Bouble infinie qui lit et affiche la température de chaque sonde | Infinite loop than read and print temperature of each probe
while True:
    print('temperatures:', end=' ')
    ds.convert_temp()
    temps = []
    for rom in roms:
        temp = ds.read_temp(rom)
        temps.append(temp)
        print(temp, end=' ')
    if max(temps) > 28:
        led.off()
    else:
        led.on()

    print()
    time.sleep_ms(1000)