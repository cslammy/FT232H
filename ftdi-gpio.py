from pyftdi.gpio import GpioAsyncController
import time

device = 'ftdi://ftdi:232h:0:1/1'

gpioa=GpioAsyncController()

x = 0
gpioa.configure(device, direction=0b11111111)
# all pins as output; use AD0-7
#pins AC0-9 don't work with bit bang GPIO?

#flash LED 4 times


while (x != 4):
    gpioa.write(0b00000000)

    time.sleep(1) # Sleep for 1 second
    gpioa.write(0b11111111)
    time.sleep(1) # Sleep for 1 second
    print("iter value is: " + str(x))
    x=x+1
