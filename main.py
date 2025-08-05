from machine import Pin 
from utime import sleep

# ------------------------------------ #

led_yellow = Pin (14, Pin.OUT)

led_green  = Pin (12, Pin.OUT)

led_red    = Pin (15, Pin.OUT)

while True:
    led_green.on()
    print("Green LED ON")
    sleep(20)
    led_green.off()
    print("Green LED OFF")

    #Pause 0.5 sec
    sleep(0.5)

    led_yellow.on()
    print("Yellow LED ON")
    sleep(10)
    led_yellow.off()
    print("Yellow LED OFF")

    #Pause 0.5 sec
    sleep(0.5)

    led_red.on()
    print("Red LED ON")
    sleep(7)
    led_red.off()
    print("Red LED OFF")

    #Pause 0.5 sec
    sleep(0.5)

# 20 segundos para Verde
# 10 segundos para Amarelo
# 7 segundos para Vermelho
# sleep entre eles de 0.5
# Dentro de um laço de repetição.