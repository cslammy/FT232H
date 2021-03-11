
'''
# WHAT THIS DOES
# SPI reads of Microchip MCP3008
# 4 OR 8 channel 10 bit ADC.
# PDIP still around for sale.
# Thank goodness!

HOW TO CONNECT TO SPI MASTER
ad0 SCLK to MCP3008 13
ad1 MOSI to MCP3008   11
ad2 MISO to MCP3008 pin 12
ad3 CS0 to 10

what pins do on MCP3008:
Pin 1-8 ADC ins, channel 0-7
GND: 9,14
5V 16
5V 15 (13 is vref)

'''
import time
from pyftdi.spi import SpiController
spi = SpiController(cs_count=2)
device = 'ftdi://ftdi:232h:0:1/1'
# Configure the first interface (IF/1) of the FTDI device as a SPI master
spi.configure(device)

# Get a port to a SPI slave w/ /CS--SPI mode 0
slave = spi.get_port(cs=0, freq=8E5, mode=0)
# second byte: which channel to read
#this assumes single ended mode
#refer to datasheet for 4 channel diff mode.
chan0 = 0b10000000
chan1 = 0b10010000
chan2 = 0b10100000
chan3 = 0b10110000
chan4 = 0b11000000
chan5 = 0b11010000
chan6 = 0b11100000
chan7 = 0b11110000

yy = chan0

qq = bytearray([1,yy,255])

# Synchronous full duplex exchange with the remote SPI slave
# dookie out, more dookie in

count = 0

while (count < 100):

    write_buf = qq
    read_buf = slave.exchange(write_buf, duplex=True)
    #read = slave.exchange(out=qq, readlen=0, start=True, stop=False, duplex=True, droptail=0)
    #slave.flush()
    x = read_buf[0]
    y = read_buf[1] - 248
    z = read_buf[2]
    dec = (y * 256) + z
    #print(x,y,z)
    displaychan = yy - 128
    print("Output from channel " + str(displaychan) + " is: " + str(dec))
    time.sleep(.5)
    count = count + 1