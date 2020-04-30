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


# Request i2c data from drive
while True:
	data = drive.read(0x0,12)	#address and buffer size
	print(data)
