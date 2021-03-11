from pyftdi.spi import SpiController

#pinout from H232 for SPI
'''
ad0 SCLK max9939 pin 1
ad1 MOSI max9939 pin 2
ad2 MISO N/C
ad3 CS0 N/C
ad4 CS max9939 pin 10  
use 5V pullups for all data lines.

setting gain for 9939
D5 don't care
D6,7 always 0


D0---D4
gain boost!!!
10000 gain 1
10101 gain 1
11000 gain 10
10100 gain 20
10011 gain 30
10010 gain 40
11010 gain 60
10110 gain 80
11110 gain 157

gain cut!!!
11001 gain .2 with Vcc at 5V
11001 gain .25 with Vcc at 3.3V
'''

# Instantiate a SPI controller
# We need want to use A*BUS4 for /CS, so at least 2 /CS lines should be
# reserved for SPI, the remaining IO are available as GPIOs.
spi = SpiController(cs_count=2)
device = 'ftdi://ftdi:232h:0:1/1'
# Configure the first interface (IF/1) of the FTDI device as a SPI master
spi.configure(device)
a = 0b00000000 #voltage offset when left bit (D0) is zero. D1-D5 determine offset. D7 is shutdown. D6 turns off inputs
# for measuring offset.

b = 0b11001000 #gain when left bit (D0) is one. D1-D4 determine gain.  D7 is shutdown.

# Get a port to a SPI slave w/ /CS on A*BUS4 and SPI mode 2 @ 10MHz
slave = spi.get_port(cs=1, freq=8E5, mode=0)
qq = bytearray([b])
#qq = bytearray([a])
# Synchronous exchange with the remote SPI slave
#write_buf = qq
#read_buf = slave.exchange(write_buf, duplex=False)
slave.exchange(out=qq, readlen=0, start=True, stop=False, duplex=False, droptail=0)
slave.flush()