import ctypes
import pylibi2c
import time

#MAKE A CLASS FOR JOINTS.. on a personal note, I'd never ever felt the need to get into OOP until now. Making this "joint" class makes things so much easier.
class joint:	#In robotics parlace we think of each motor as a joint
	def __init__(self, name, address, channel):
		self.name = name	#a colloquial name for this joint
		self.address = address #the I2C address of the NearZero controlling this motor/joint
		self.channel = channel	#the NearZero channel that the motor/joint is wired to
	def i2cSetup(self):
		self.address = pylibi2c.I2CDevice('/dev/i2c-1', self.address) # Open i2c device with the correct bus and at the given address
		self.address.delay = 10 # Set delay
		self.address.page_bytes = 16 # Set page_bytes
		self.address.flags = pylibi2c.I2C_M_IGNORE_NAK # Set flags
	def write(self,mode,VelPos,I):
		if abs(VelPos)< 10:		#make leading zeros depending on size of input
			vpleader = "0000"
		elif abs(VelPos)< 100:
			vpleader = "000"
		elif abs(VelPos)< 1000:
			vpleader = "00"
		elif abs(VelPos)< 10000:
			vpleader = "0"
		if VelPos >= 0:		#choose sign based on value of VelPos
			sign = "+"
		else:
			sign = "-"
		VelPos = str(abs(VelPos))
		if I < 10:		#make leading zeros depending on size of input
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


#INSTANTIATE THE JOINTS
LeftWheel = joint("LeftWheel",0x40,"1")
RightWheel = joint("RightWheel",0x40,"2")
HeadYaw = joint("HeadYaw",0x41,"1")
HeadPitch = joint("HeadPitch",0x41,"2")
HeadRoll = joint("HeadRoll",0x42,"1")

#START THE I2C SERVICE FOR EACH I2C ADDRESS
LeftWheel.i2cSetup()
RightWheel.i2cSetup()
HeadYaw.i2cSetup()
HeadPitch.i2cSetup()
HeadRoll.i2cSetup()


def move():	#This function takes in v_x and v_th and calculates the velocity for each wheel and writes it to each wheel
	vel1 = v_x + v_th
	vel2 = v_x - v_th
	LeftWheel.write('s',vel1,100)
	RightWheel.write('s',vel2,100)

#DRIVE THE ROBOT
HeadYaw.write('p',-100,100);
HeadPitch.write('p',200,100);
HeadRoll.write('p',100,0);

v_x = 30
v_th = 0
move()

#for v_x in range(0,2000,40):
#	move()

#for v_x in range(2000,0,-40):
#	move()
