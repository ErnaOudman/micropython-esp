Working flash:
C:\Users\ernao\Downloads>esptool --port COM5 --baud 115200 write_flash -fm dio --flash_size=detect 0 esp8266-20180511-v1.9.4.bin

Using the OLED screen:
https://www.instructables.com/id/MicroPython-on-an-ESP32-Board-With-Integrated-SSD1/

Copy .py file to ESP:
ampy --port COM5 --baud 115200 -d 0.5 put ssd1306.py
