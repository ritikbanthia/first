import RPi.GPIO as io 
from time import sleep 
io.setmode(io.BCM)

io.setup(18,io.IN)
io.setup(4,io.OUT)
io.setup(2,io.OUT)
io.setup(3,io.OUT)

for i in range(2,5):
	io.output(i,False)


count = 0
status = 0
while True :
	while status == 1:
		sleep(.01)
		if count == 100:
			io.output(2,True)
		if count == 200:
			io.output(4,True)
		if count ==  300:
			io.output(3,True)
		count = count + 1
		status = io.input(18)
	count = 0
	for i in range(2,5):
		io.output(i,False)
	status = io.input(18)
