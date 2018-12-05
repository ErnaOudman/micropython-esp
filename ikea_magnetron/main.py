import tm1637
from machine import Pin
import time
tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))

# all LEDS on "88:88"
tm.write([127, 255, 127, 127])
time.sleep(2)

# all LEDS off
tm.write([0, 0, 0, 0])
time.sleep(2)

# show "0123"
# tm.write([63, 6, 91, 79])
# time.sleep(2)

# show "COOL"
# tm.write([0b00111001, 0b00111111, 0b00111111, 0b00111000])
# time.sleep(2)

# # show "HELP"
# tm.show('help')
# time.sleep(2)

# # display "dEAd", "bEEF"
# tm.hex(0xdead)
# tm.hex(0xbeef)
# time.sleep(2)

# # show "12:59"
# tm.numbers(22,15)
# time.sleep(2)

# # show "-123"
# tm.number(-123)
# time.sleep(2)

# # show temperature '24*C'
# tm.temperature(20)
# time.sleep(2)

# Rotary encoder
from rotary_irq_esp import RotaryIRQ
r = RotaryIRQ(
    pin_num_clk=14,
    pin_num_dt=12,
    min_val=0,
    max_val=200,
)
while True:
    print(r.value())