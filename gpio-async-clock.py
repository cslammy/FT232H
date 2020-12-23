#FT232H as GPIO clock gen.



from pyftdi.gpio import GpioAsyncController

gpioa=GpioAsyncController()

device = 'ftdi://ftdi:232h:0:1/1'

gpioa.configure(device, direction=0b11111111)



bytes = []



#works with pins AD0-AD7

#output goes from hi-z to ground, so you may need to set up a pullup.

#you might need to buffer the output of AD0 (with transistor?)  depending on what you have downstream. For my scope I didn't need it.

#dont remember why I commented next line but

#it isn't needed.

#gpioa.open_from_url(device, direction=0b11111111)





freq=100000 #keep this reasonable. < 500K.

secs = 5 # number of seconds to run clock.

#resulting frequency of on followed by off is half of freq.

#so we mult it by 2....

gpioa.set_frequency(freq*2)



#GPIO outputs are sent as an array of bytes.

#below we create 10K bytes alternating off and on, and output the data enough

#times to create a secs second pulse.

a = range(0,10000)



for b in a:

    if b % 2 == 0:

        bytes.append(0x0)

    else:

        bytes.append(0x1)



times = int(freq/10000)

print(times)

#WRITE YER BYTES FOR "secs" SECONDS

a = range(0,times*secs)

for xx in a:



   gpioa.write(bytes)
