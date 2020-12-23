
from pyftdi.i2c import I2cController
i2c = I2cController()


device = 'ftdi://ftdi:232h:0:1/1'


slave_port = (0x62)
i2c.configure(device)
a = i2c.get_port(slave_port)

#create a crappy ramp wave....
rList = [0,255,1,255,2,255,3,255,4,255,5,255,6,255,7,255,8,255,9,255,0xA,255,0xB,255,0xC,255,0xD,255,0xE,255,0xF,255]

#run it 1000x's
arr = bytearray(rList)
b = 0
while b < 1000:
    a.write(arr,relax=False)

    b = b + 1
