import pyftdi.serialext
from pyftdi.ftdi import Ftdi


Ftdi.show_devices()
##returns this.  12-12-20 10:25AM
##Available interfaces:
##ftdi://ftdi:232h:0:1/1   (Single RS232-HS)
port = pyftdi.serialext.serial_for_url('ftdi://ftdi:232h:0:1/1', baudrate=9600)

# Send bytes

port.write(b'Hello Arduino 9I am still here')
