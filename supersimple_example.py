import ctypes
import pylibi2c
import time

drive = pylibi2c.I2CDevice('/dev/i2c-1', 0x40) # Open i2c device at address 0x3
drive.delay = 10 # Set delay
drive.page_bytes = 16 # Set page_bytes
drive.flags = pylibi2c.I2C_M_IGNORE_NAK # Set flags

head = pylibi2c.I2CDevice('/dev/i2c-1', 0x41) # Open i2c device at address 0x4
head.delay = 10 # Set delay
head.page_bytes = 16 # Set page_bytes
head.flags = pylibi2c.I2C_M_IGNORE_NAK # Set flags

huh = pylibi2c.I2CDevice('/dev/i2c-1', 0x42) # Open i2c device at address 0x5
huh.delay = 10 # Set delay
huh.page_bytes = 16 # Set page_bytes
huh.flags = pylibi2c.I2C_M_IGNORE_NAK # Set flags


# Write data to i2c
#CHAN,MODE,SIGN,CMD,CMD,CMD,CMD,CMD,"C",CMD,CMD,CMD,CMD,CMD
drive.write(0x0, '1s+00000c00200')	#Left wheel
drive.write(0x0, '2s+00000c00200')	#Right wheel

#head.write(0x0, '1p+00000c00000')	#Azimuth, +RIGHT / -LEFT
#head.write(0x0, '2p+00000c00000')	#Altitude 

#huh.write(0x0, '1p+00000c00100')	#Roll
#huh.write(0x0, '2s-00300c00010')	#Aux

#time.sleep(1)

# Request i2c data from drive
while True:
	data = drive.read(0x0,12)	#address and buffer size
	print(data)
