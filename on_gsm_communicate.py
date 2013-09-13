import time
import sys
import serial

mobileno = ['+919XXXXXXXXX']
phone = serial.Serial()

phone.port="/dev/ttyACM0"
phone.baudrate=9600
phone.timeout=9
phone.xonxoff = False
phone.rtscts = False
phone.bytesize = serial.EIGHTBITS
phone.parity = serial.PARITY_NONE
phone.stopbits = serial.STOPBITS_ONE

def get_num(x):
   return str(''.join(ele for ele in x if ele.isdigit()))

def recept(message, recipient):
   time.sleep(0.5)
   phone.write('AT\r\n')
   time.sleep(0.5)
   phone.write('AT+CMGF=1\r\n')
   time.sleep(0.5)
   phone.write('AT+CMGW="'+recipient+'"\r\n')
   out = ''
   time.sleep(1)
   while phone.inWaiting() > 0:
      out += phone.read(1)
   if out != '':
      print ">>" + out
   phone.write(message)
   phone.write('\x1a')
   out = ''
   time.sleep(1)
   while phone.inWaiting() > 0:
      out += phone.read(1)
   if out != '':
      print ">>" + out
   number = get_num(out)
   phone.write('AT+CMSS='+number+'\r\n')
   out = ''
   time.sleep(1)
   while phone.inWaiting() > 0:
      out += phone.read(1)
   if out != '':
      print ">>" + out

def sendSMS(message):
  try:
   phone.open()
   phone.flushInput()
   phone.flushOutput()
   for row in mobileno:
    time.sleep(0.5)
    mobile = row
    recept(message, mobile)
   time.sleep(1)
   phone.write('AT+CMGD=1,4\r\n')
   phone.close()
  finally:
   phone.close()

message = "hi"
sendSMS(message)
