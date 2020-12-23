from pyftdi.spi import SpiController

#pinout from H232 for SPI
'''
ad0 SCLK 9833 SCLK
ad1 MOSI to 9833 SDATA
ad2 MISO  (not used)
ad3 (not used)
ad4 SS to 9833 FSYNC
'''

# Instantiate a SPI controller
# We need want to use A*BUS4 for /CS, so at least 2 /CS lines should be
# reserved for SPI, the remaining IO are available as GPIOs.
spi = SpiController(cs_count=2)
device = 'ftdi://ftdi:232h:0:1/1'
# Configure the first interface (IF/1) of the FTDI device as a SPI master
spi.configure(device)

# Get a port to a SPI slave w/ /CS on A*BUS4 and SPI mode 2 @ 10MHz
slave = spi.get_port(cs=1, freq=8E6, mode=2)

cntrl_reset = [33,0]

#freq0_loadmsb = [80,199] # 400hz.
freq0_loadreg = [120,00] #1.33khz
#freq0_loadreg = [123,FF] #3.1Mhz

cntrl_freq0write = [64,0]

phase0 = [192,0]

cntrl_write = [32,0]

send2_9833 = cntrl_reset + freq0_loadreg + cntrl_freq0write + phase0 + cntrl_write

print(send2_9833)

qq = bytearray(send2_9833)
# Synchronous exchange with the remote SPI slave
#write_buf = qq
#read_buf = slave.exchange(write_buf, duplex=False)
slave.exchange(out=qq, readlen=0, start=True, stop=True, duplex=False, droptail=0)
slave.flush()