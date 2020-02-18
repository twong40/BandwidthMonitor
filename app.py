import psutil
import math
import time
#class for individial graphing 
class NetworkType:
    def __init__(self):
        self.dataIn = 0
        self.dataOut = 0
    
    def getIn(self):
        return convert_size(self.dataIn)
    
    def getOut(self):
        return convert_size(self.dataOut)

    def addDataIn(self, data):
        self.dataIn+= data

    def addDataOut(self, data):
        self.dataOut+= data

# TODO
# 1) Create a mapping so that it shows how much it increased per time instead of total
# 2) Add that feature into the class so each type of network can be graphed
# 3) Use a pandas library or similar to graph the recorded trend in bandwidth usage
def main():
    ET = NetworkType()
    LAC = NetworkType()
    WIFI = NetworkType()
    BT = NetworkType()
    LP = NetworkType()
    LO = NetworkType()
    totalOut = 0
    totalIn = 0
    while True:
        data = psutil.net_io_counters(pernic=True)
        localtime = time.asctime( time.localtime(time.time()) )
        for key in data:
            dataOut = data[key][0]
            dataIn = data[key][1]
            totalOut+= dataOut
            totalIn+= dataIn
            if "Ethernet" in key or "eth" in key:
                ET.addDataIn(dataIn)
                ET.addDataOut(dataOut)
            elif "Local Area Connection" in key or "lan" in key:
                LAC.addDataIn(dataIn)
                LAC.addDataOut(dataOut)
            elif "Wi-Fi" in key:
                WIFI.addDataIn(dataIn)
                WIFI.addDataOut(dataOut)
            elif "Bluetooth" in key:
                BT.addDataIn(dataIn)
                BT.addDataOut(dataOut)
            elif "Loopback" in key:
                LP.addDataIn(dataIn)
                LP.addDataOut(dataOut)
            elif "lo" in key:
                LO.addDataIn(dataIn)
                LO.addDataOut(dataOut)
        print("Local Time: " + localtime + "\n" + convert_size(totalOut) + " sent\n" + convert_size(totalIn) + " received")

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
if __name__ == "__main__":
    main()