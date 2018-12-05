import tm1637
from machine import Pin
import time
tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))

# Rotary encoder
from rotary_irq_esp import RotaryIRQ
r = RotaryIRQ(
    pin_num_clk=14,
    pin_num_dt=12,
    min_val=0,
    max_val=200,
)

while True:
    cur_val = r.value()
    # print(r.value())
    minutes = int(cur_val/60)
    seconds = cur_val%60
    tm.numbers(minutes,seconds)
    time.sleep(.1)
   