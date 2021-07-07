import os, time, datetime
from datetime import date
from datetime import datetime
import requests

sn = '0000004342'
delayTime = 3600*24

###### Open tranmission rank ######
try:
    tests = dict()
    file = open("TranmissionRank.txt")
    for line in file:
        line = line.rstrip().split(",")
        tests[line[0]] = line[1]
except:
    print("Missing Tranmission Rank file. Please check")

while True:

    today = date.today()
    now = datetime.now()
    print("Now: ", now)
    today_string = today.strftime("%Y%m%d")
    today_string2 = today.strftime("%d/%m/%y")
    today_string3 = today.strftime("%d/%m/%Y")
    str_day = today.strftime("%d")
    str_month = today.strftime("%m")
    str_year = today.strftime("%Y")

    fileName = "Pilot001-" + today.strftime("%y%m%d") + ".TRA"
    folderPath = "C:\\pilote\\autom\\"
    path = folderPath + "Pilot001-210706.TRA"
    print(path)
    print(now)

    currentID = ""
    test = "0"
    count = 0
    try:
        file = open(path, "r")
        for line in file:
            if line.startswith("---------- "):
                line = line.rstrip()
                timeStr = line[11:30]
                recordTime = datetime.strptime(timeStr,'%d/%m/%Y %H:%M:%S')
                diffTime = (now -recordTime).total_seconds()
                
                line = line[34:]
                #print(line)
                if line.startswith("Id patient"):
                    if currentID != line:
                        print(count)
                        print(currentID)
                        currentID = line.split(": ")[1]
                        count = count + 1
                        test = "0"
                if line.startswith("Test"):
                    rank = line.split(" ")[1]
                    #print("Rank: ", rank)
                    #print("last test: ",test)
                    if tests[rank] != test:
                        test = tests[rank]
                        msg = timeStr + " / " + currentID + " " + test
                        print(msg)
                        url = "http://datamedigroup.com/MG/addsce1.php?sn="+sn+"&data="+msg
                        #x = requests.post(url)
                        #print(url)
    except:
        print("error")
    print("Total sample: ", count)
    time.sleep(delayTime)
