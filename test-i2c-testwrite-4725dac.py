
from pyftdi.i2c import I2cController
i2c = I2cController()


device = 'ftdi://ftdi:232h:0:1/1'

'''
YOu need 2 byte addr. of your i2c dookie.

use "i2cscan.py" to get the
address of your I2C device.

i2cscan.py is in the "tools" included with
pyftdi

However you need to modify i2cscan.py first.
find this line, then put your URL here:
argparser.add_argument('device', nargs='?', default='[YOUR-FTDI-URL-HERE]'

OK run the i2cscan.py script

output of that program is a grid with a single char, not a value.
Q: what do x and y axis in the grid mean?
A: it indicates the address where it found your I2C device.
to craft hex addr of device it's:0x(column row)
you knew that right?
'''
slave_port = (0x62)
i2c.configure(device)
a = i2c.get_port(slave_port)
#'0x0F,0XFF is full throttle'
#'0x00,0x00 means 0V from DAC out'
a.write([0x01,0xFF])
