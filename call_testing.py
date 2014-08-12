import serial
ser = serial.Serial("/dev/ttyACM0", 460800)
import time

class PhoneConnection:

    def connectPhone(self):
                self.ser = serial.Serial('/dev/ttyACM0', 460800, timeout=5, xonxoff = False, rtscts = False, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE)
                time.sleep(1)

    def openPort(self):
                self.ser.close()
                self.ser.open()

    def disconnectPhone(self):
                self.ser.close()
                self.ser.open()

class DataCall:

        #Additional function to check PIN
        def checkPIN(self):
                self.ser = serial.Serial("/dev/ttyACM0", 460800)
                self.ser.write(b'ATZ\r\n')
                ## ATZ : Restore profile ##
                time.sleep(1)
                self.ser.write(b'AT+CPIN\r\n')
                time.sleep(1)
                self.ser.write(bytes(26))
                time.sleep(1)
                
        #Additional function to check registration status of the device
        def checkSTATUS(self):
                self.ser.write(b'ATZ\r\n')
                ## ATZ : Restore profile ##
                time.sleep(1)
                self.ser.write(b'AT+CGREG\r\n')
                time.sleep(1)
                self.ser.write(bytes(26))
                time.sleep(1)
                
        #Additional function to check signal
        def checkSIGNAL(self):
                self.ser.write(b'ATZ\r\n')
                ## ATZ : Restore profile ##
                time.sleep(1)
                self.ser.write(b'AT+CSQ\r\n')
                time.sleep(1)
                self.ser.write(bytes(26))
                time.sleep(1)
                
        #Additional function to check GPRS
        def checkGPRS(self):
                self.ser.write(b'ATZ\r\n')
                ## ATZ : Restore profile ##
                time.sleep(1)
                self.ser.write(b'AT+CGATT=1\r\n')
                time.sleep(1)
                self.ser.write(bytes(26))
                time.sleep(1)
                
        #Additional function to check Packet Data Protocol (PDP)
        def checkPDP(self):
                self.ser.write(b'ATZ\r\n')
                ## ATZ : Restore profile ##
                time.sleep(1)
                #set the APN here like epc.tmobile.com
                self.ser.write(b'AT+CGDCONT=1,"IP","epc.tmobile.com"\r\n')
                time.sleep(1)
                self.ser.write(bytes(26))
                time.sleep(1)
                
        #Additional function to check activation
        def checkACTIVATE(self):
                self.ser.write(b'ATZ\r\n')
                ## ATZ : Restore profile ##
                time.sleep(1)
                self.ser.write(b'AT+CGACT=1,1\r\n')
                time.sleep(1)
                self.ser.write(bytes(26))
                time.sleep(1)   
                
        #Additional function to check deactivation
        def checkDEACTIVATE(self):
                self.ser.write(b'ATZ\r\n')
                ## ATZ : Restore profile ##
                time.sleep(1)
                self.ser.write(b'AT+CGACT=0,1\r\n')
                time.sleep(1)
                self.ser.write(bytes(26))
                time.sleep(1)
                
        #Additional function to check dettachment of GPRS
        def checkDEGPRS(self):
                self.ser.write(b'ATZ\r\n')
                ## ATZ : Restore profile ##
                time.sleep(1)
                self.ser.write(b'AT+CGATT=0\r\n')
                time.sleep(1)
                self.ser.write(bytes(26))
                time.sleep(1)

class VoiceCall:

    def __init__(self, mobileNumber="09967066261"):
        self.mobileNumber = mobileNumber
     #08976158319   
    def setRecipient(self, number):
        self.mobileNumber = number        
        
    def dialNumber(self):
        self.ser = serial.Serial("/dev/ttyACM0", 460800)
        self.ser.write(b'ATZ\r\n')
        ## ATZ : Restore profile ##
        time.sleep(1)
        self.ser.write(b'ATDT' + self.mobileNumber.encode() + b';\r\n')
        ## ATD : Dial command ##
        time.sleep(1)
        time.sleep(25)
        self.ser.write(bytes(26))
        time.sleep(25)
        time.sleep(1)
        time.sleep(1)

    def endCall(self):
        self.ser.write(b'ATZ\r\n')
        time.sleep(1)
        self.ser.write(b'AT+CHUP\r\n')
        time.sleep(1)
        self.ser.write(bytes(26))
        time.sleep(1)

    def disconnectPhone(self):
        self.ser.close()

phone = PhoneConnection()
phone.connectPhone()
print ("Phone Connected")
phone.openPort()
print ("Port Opened")

data = DataCall()
phone.openPort()
print ("Port Opened")
data.checkPIN()

print ("Checking PIN success")
data.checkSTATUS()
print ("Checking Status success")
data.checkSIGNAL()
print ("Checking Signal success")
data.checkGPRS()
print ("Checking GPRS success")
data.checkPDP()
print ("Checking PDP success")
data.checkACTIVATE()
print ("Activation success")
data.checkDEACTIVATE()
print ("Deactivation success")
data.checkDEGPRS()
print ("GPRS Closed")

call = VoiceCall("09967066261")
call.dialNumber()
print ("Call Connected")
call.endCall()
print ("Call Ended")

phone.disconnectPhone()
print ("Phone Disconnected")
