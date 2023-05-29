from machine import ADC
import time

sensor = ADC(4)


while True:
    valor = sensor.read_u16()*3.3/65535
    temp = 30-(valor-0.706)/0.001721
    print(temp)
    time.sleep(4)
