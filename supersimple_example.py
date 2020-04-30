import ctypes
import pylibi2c
import time

#------CONNECT TO NZ AT GIVEN ADDRESS (e.g. 0x40) AND GIVE IT A NAME (e.g. "wheels")------
wheels = pylibi2c.I2CDevice('/dev/i2c-1', 0x40) 
wheels.delay = 10 
wheels.page_bytes = 16 
wheels.flags = pylibi2c.I2C_M_IGNORE_NAK 

#------CONNECT TO ANOTHER NZ WITH A DIFFERENT ADDRESS AND NAME----------------------------
#head = pylibi2c.I2CDevice('/dev/i2c-1', 0x41) 
#head.delay = 10 
#head.page_bytes = 16 
#head.flags = pylibi2c.I2C_M_IGNORE_NAK 


#------WRITE COMMANDS TO NEARZERO---------------------------------------------------------
#(0x0, 'CHAN(1/2) MODE(v/p/s) SIGN(+/-) CMD CMD CMD CMD CMD "C" CMD CMD CMD CMD CMD')
wheels.write(0x0, '1v+00100c00200')	#Drive channel 1 at velocity=100 with 200mA of current
wheels.write(0x0, '2v+00250c00320')	#Drive channel 2 at velocity=250 with 320mA of current

#head.write(0x0, '1p+00000c00000')	#Drive channel 1 at position=0 with 0mA of current
#head.write(0x0, '2p+01000c00600')	#Drive channel 2 at position=1000 and 600mA of current 


