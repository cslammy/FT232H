'''
PYFTDI shakeout code for Microchip MCP4922
This is dual channel 12 bit DAC 14 pin PDIP (yeh! go PDIP!)

HOW TO CONNECT TO SPI MASTER (FTDI232H)
HOW TO CONNECT TO SPI MASTER
ad0 SCLK to MCP4922  pin 4
ad1 MOSI to MCP4922 pin 5
ad2 MISO No Connection
ad3 CS0 to MCP4922 pin 3

HOW TO WIRE UP MCP4922
5V to Pins 1 (Vdd) 9 (shutdown, hold this high)
5V to 11 and 13 (reference for DAC)
GND to 12 (Vss) and 8 (latch)
3 is CS
4 is Ser. clock
5 is MOSI
14 OUTPUT DAC A
10 OUTPUT DAC B

'''

def getlsb(input):
    x = input%256
    return x

def getmsb(input,chan):

    y = input/256
    if (chan == 0):
         y = int(y) + 0b00110000  #DAC0,unbuff ref, 1xgain, no shutdown
    else:
        y = int(y) + 0b10110000 #DAC1 unbuff ref, 1x gain, no shutdown
    return y


b = range(0,4096,16)
for value in b:
    msb = getmsb(value,0)
    lsb = getlsb(value)
    print("mapping value " + str(value)  + " as " + str(msb) + " " + str(lsb))

    from pyftdi.spi import SpiController
    spi = SpiController(cs_count=2)  #AD3 and 4 used for CS
    device = 'ftdi://ftdi:232h:0:1/1'
    # Configure the first interface (IF/1) of the FTDI device as a SPI master
    spi.configure(device)
    # Get a port to a SPI slave w/ /CS on AD3 and SPI mode 0 @ 10MHz
    slave = spi.get_port(cs=0, freq=8E5, mode=0)
    qq = bytearray([msb,lsb])
    # Synchronous exchange with the remote SPI slave
    #write_buf = qq
    #read_buf = slave.exchange(write_buf, duplex=False)
    slave.exchange(out=qq, readlen=0, start=True, stop=False, duplex=False, droptail=0)
    slave.flush()
