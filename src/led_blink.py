import machine
import time

internal_led = machine.Pin("LED", machine.Pin.OUT)

external_led = machine.Pin(15, machine.Pin.OUT)

while True:
    internal_led.on()
    external_led.on()
    time.sleep(1)  

    internal_led.off()
    external_led.off()
    time.sleep(1) 

