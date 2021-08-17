import sys
import time
import subprocess
import os

bytetime = float(0)
accuracy = 100

bytetimes = float(0)

def getbytetime(testfilename):
    try:
        filesize = os.stat(testfilename).st_size
    except:
        print("Please create an example program , for example : printing 100 number or something like that, please make it an executable ,and it's prefered to not use any kind of optimizations , call it 'example' or change the name on the source file to what suits you")
        sys.exit()
        
    stime_ns = time.time_ns() / 1000000 / filesize
    
    subprocess.run([testfilename], stdout=subprocess.PIPE)
    etime_ns = time.time_ns() / 1000000 / filesize

    return float(etime_ns - stime_ns)


def setbytetime():
    global bytetimes
    global bytetime
    
    for i in range(accuracy):
        bytetimes += getbytetime("./example")

    bytetime = float(bytetimes / accuracy)
    with open("bytetime.txt","w") as f:
        f.write(str(bytetime))


def main():
    try:
        bytetime = float(open("bytetime.txt","r").read()) 
    except:
        setbytetime()
        print("Please restart the program")
        sys.exit("")
    
    print("Time in ms : ",bytetime * os.stat(sys.argv[1]).st_size)




main()
