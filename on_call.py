import time
import sys
import serial

mobileno = '8XXXXXXXXX'
phone = serial.Serial()

phone.port="/dev/ttyACM0"
phone.baudrate=9600
phone.timeout=9
phone.xonxoff = False
phone.rtscts = False
phone.bytesize = serial.EIGHTBITS
phone.parity = serial.PARITY_NONE
phone.stopbits = serial.STOPBITS_ONE

#Dialing out and hanging up a voice call using ATD command on Nokia Phone
phone.open()
phone.flushInput()
phone.flushOutput()
time.sleep(0.5)
phone.write('AT\r\n')
time.sleep(0.5)
phone.write('ATD '+mobileno+';\r\n')
out = ''
time.sleep(1)
while phone.inWaiting() > 0:
   out += phone.read(1)
if out != '':
   print ">>" + out
