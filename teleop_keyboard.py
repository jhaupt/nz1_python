import ctypes, pylibi2c, time, sys, termios, tty, os

#---------------------MAKE A CLASS FOR THE NEARZERO-----------------------------------
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
		if I < 10: 			#make leading zeros depending on value of I
			Ileader = "0000"
		elif I < 100:
			Ileader = "000"
		elif I < 1000:
			Ileader = "00"
		elif I < 10000:
			Ileader = "0"
		I = str(I)
		i2c_out = self.channel+mode+sign+vpleader+VelPos+'c'+Ileader+I	#concatenate the channel, sign, and command value
		self.address.write(0x0, i2c_out)	#Write to ic2

#-------------INSTANTIATE THE JOINTS-------------------------------
LeftWheel = nz("LeftWheel",0x40,"1")
RightWheel = nz("RightWheel",0x40,"2")
#HeadYaw = nz("HeadYaw",0x41,"1")
#HeadPitch = nz("HeadPitch",0x41,"2")

#-----------START THE I2C SERVICE FOR EACH I2C ADDRESS--------------
LeftWheel.i2cSetup()
RightWheel.i2cSetup()
#HeadYaw.i2cSetup()
#HeadPitch.i2cSetup()


def move():	#This function takes in v_x and v_th and calculates the differential drive velocity for each wheel and writes it to each wheel
	vel1 = -1*(v_x + v_th)
	vel2 = v_x - v_th
	I1 = 1*int(abs(vel1))	#simple current scaling
	I2 = 1*int(abs(vel2))
	print("I1="),
	print(I1),
	print("A")
	print("I2="),
	print(I2),
	print("A")
	print(" ")
	if vel1 == 0:
		I1 = 0
	if vel2 == 0:
		I2 = 0
	LeftWheel.write('v',vel1,I1)
	RightWheel.write('v',vel2,I2)

def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)

	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

print('w = increment forward velocity')
print('s = increment backward velocity')
print('a = increment left steering')
print('d = increment right steering')
print('x = freeze')
print('')
print('i = point head up')
print('m = point head down')
print('j = point head left')
print('k = point head right')
print('o = head motors off')
print('')
print('q = quit')


v_x = 0
v_th = 0
y = 0
p = 0
r = 0

while True:
	char = getch()
	if (char == "q"):
		exit(0)
	if (char == "w"):
		v_x = v_x + 20
		move()
	elif (char == "a"):
		v_th = v_th - 10
		move()
	elif (char == "s"):
		v_x = v_x - 20
		move()
	elif (char == "d"):
		v_th = v_th + 10
		move()
	elif (char == "x"):
		v_x = 0
		v_th = 0
		move()
	elif (char == "i"):
		p = p + 150
		HeadPitch.write('p',p,50)
	elif (char == "m"):
		p = p - 150
		HeadPitch.write('p',p,50)
	elif (char == "j"):
		y = y - 500
		HeadYaw.write('p',y,50)
	elif (char == "k"):
		y = y + 500
		HeadYaw.write('p',y,50)
	elif (char == "h"):
		r = r - 100
		HeadRoll.write('p',r,50)
	elif (char == "l"):
		r = r + 100
		HeadRoll.write('p',r,10)
	elif (char == "o"):
		HeadPitch.write('p',p,0)
		HeadYaw.write('p',y,0)
		HeadRoll.write('p',r,0)

	#UNCOMMENT BELOW TO DISPLAY ENCODER DATA EVERY TIME A KEYPRESS IS ENTERED
	#odom = LeftWheel.address.read(0x0,12)
	#print(odom)
