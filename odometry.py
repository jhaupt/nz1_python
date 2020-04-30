import ctypes
import pylibi2c
import time

#------CONNECT TO NZ AT GIVEN ADDRESS (e.g. 0x40) AND GIVE IT A NAME (e.g. "wheels")----
wheels = pylibi2c.I2CDevice('/dev/i2c-1', 0x40) # Open i2c device at address 0x3
wheels.delay = 10 # Set delay
wheels.page_bytes = 16 # Set page_bytes
wheels.flags = pylibi2c.I2C_M_IGNORE_NAK # Set flags

#------CONNECT TO ANOTHER NZ WITH A DIFFERENT ADDRESS AND NAME---------------------------
#head = pylibi2c.I2CDevice('/dev/i2c-1', 0x41) # Open i2c device at address 0x4
#head.delay = 10 # Set delay
#head.page_bytes = 16 # Set page_bytes
#head.flags = pylibi2c.I2C_M_IGNORE_NAK # Set flags


#------READ FROM THE NEARZERO------------------------------------------------------------
while True:
	data1 = wheels.read(0x0,12)	#The last part is the buffer size; enough for 6 digits from each encoder
	print(data1)			
	
	#data2 = head.read(0x0,12)
	#print(data2)

	#The first 6 digits give the encoder value from channel 1
	#The second 6 digits give the encoder value from channel 2
	#Digits 1 and 7 indicate sign, where 0 = positive and - = negative.
