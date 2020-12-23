from pyftdi.spi import SpiController

#pinout from H232 for SPI
'''
ad0 SCLK to UNO pin 13
ad1 MOSI to UNO pin     11
ad2 MISO to UNO pin 12
ad3 CS0 to UNO pin 10
ad4 cs1 ... ad7 CS4.
'''

# Instantiate a SPI controller
# We need want to use A*BUS4 for /CS, so at least 2 /CS lines should be
# reserved for SPI, the remaining IO are available as GPIOs.
spi = SpiController(cs_count=2)
device = 'ftdi://ftdi:232h:0:1/1'
# Configure the first interface (IF/1) of the FTDI device as a SPI master
spi.configure(device)

# Get a port to a SPI slave w/ /CS on A*BUS4 and SPI mode 2 @ 10MHz
slave = spi.get_port(cs=1, freq=8E5, mode=1)
qq = bytearray([6,15])
# Synchronous exchange with the remote SPI slave
#write_buf = qq
#read_buf = slave.exchange(write_buf, duplex=False)
slave.exchange(out=qq, readlen=0, start=True, stop=False, duplex=False, droptail=0)
slave.flush()