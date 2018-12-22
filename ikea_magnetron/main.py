import tm1637
from machine import Pin
import time

tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))

button = Pin(16, Pin.IN, Pin.PULL_UP)
led = Pin(17, Pin.OUT)


# Rotary encoder
from rotary_irq_esp import RotaryIRQ
r = RotaryIRQ(
    pin_num_clk=14,
    pin_num_dt=12,
    min_val=0,
    max_val=200,
    range_mode=RotaryIRQ.RANGE_BOUNDED
)

microwave_on = False

while True:
    if microwave_on == False:
        cur_val = r.value()
    minutes = int(cur_val/60)
    seconds = cur_val%60
    tm.numbers(minutes,seconds)
    time.sleep(.2)

    if button.value() == 0:
        print('HELP')
        microwave_on = not microwave_on
        print(microwave_on)

    if microwave_on:
        cur_val -= 1
        if cur_val <= 0:
            microwave_on = False
            # LED uit
            # ping
        r._value = cur_val
        time.sleep(.8)

