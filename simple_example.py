import ctypes
import pylibi2c
import time

#-------------------MAKE A CLASS FOR THE NEARZERO----------------------------
class nz:
	def __init__(self, name, address, channel):
		self.name = name	
		self.address = address  
		self.channel = channel	
	def i2cSetup(self):
		self.address = pylibi2c.I2CDevice('/dev/i2c-1', self.address) 
		self.address.delay = 10 
		self.address.page_bytes = 16 
		self.address.flags = pylibi2c.I2C_M_IGNORE_NAK 
	def write(self,mode,VelPos,I):
		if abs(VelPos)< 10:		#make leading zeros depending on size of input
			vpleader = "0000"
		elif abs(VelPos)< 100:
			vpleader = "000"
		elif abs(VelPos)< 1000:
			vpleader = "00"
		elif abs(VelPos)< 10000:
			vpleader = "0"
		if VelPos >= 0:			#choose sign based on value of VelPos
			sign = "+"
		else:
			sign = "-"
		VelPos = str(abs(VelPos))
		if I < 10:			#make leading zeros depending on size of input
			Ileader = "0000"
		elif I < 100:
			Ileader = "000"
		elif I < 1000:
			Ileader = "00"
		elif I < 10000:
			Ileader = "0"
		I = str(I)
		i2c_out = self.channel+mode+sign+vpleader+VelPos+'c'+Ileader+I		#concatenate the channel, sign, and command value
		self.address.write(0x0, i2c_out)	#Write to ic2


#------------INSTANTIATE THE JOINTS---------------------------
LeftWheel = nz("LeftWheel",0x40,"1")
RightWheel = nz("RightWheel",0x40,"2")
#HeadYaw = nz("HeadYaw",0x41,"1")
#HeadPitch = nz("HeadPitch",0x41,"2")

#------------START THE I2C SERVICE FOR EACH I2C ADDRESS-------
LeftWheel.i2cSetup()
RightWheel.i2cSetup()
#HeadYaw.i2cSetup()
#HeadPitch.i2cSetup()


#-----------MAKE THE NEARZERO DO THINGS-----------------------------
vel1 = 300	#define velocity [unitless]
vel2 = 300
I1 = 200	#define current [mA]
I2 = 200
LeftWheel.write('v',vel1,I1)	#write the commands
RightWheel.write('v',vel2,I2)

#HeadYaw.write('p',-100,100);	
#HeadPitch.write('p',200,100);


