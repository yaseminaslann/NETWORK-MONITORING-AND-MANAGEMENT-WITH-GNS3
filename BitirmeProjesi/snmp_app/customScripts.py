import datetime
import sqlite3
from . import views
from pythonping import ping


def getDataDB():
    db = sqlite3.connect('device.sqlite3')
    dbcursor = db.cursor()
    dataDevice = dbcursor.execute('SELECT * FROM Device')
    
    deviceList = []

    for data in dataDevice:
        deviceList.append({'ip':data[0], 'username':data[1], 'password':data[2]})
    
    return deviceList



def getQueryOneOutput(Query):
    db = sqlite3.connect('device.sqlite3')
    dbcursor = db.cursor()
    dataDevice = dbcursor.execute(Query)
    
    for data in dataDevice:
        dataOut = data[0]
    return dataOut

def getCPUValue(ip, username, password):
    timeList = []
    cpuValueList = []
    kontrol = 0

    while kontrol<= 5:
        valueData = views.get_netmiko_data(ip, username, password, command='show processes cpu | include one minute')
        if 'CPU' in valueData:
            cpuValue = int(valueData.split('one minute:')[1].split('; five minutes')[0].replace('%','').strip())
            cpuValueList.append(cpuValue)
            timeList.append(kontrol)
            kontrol += 1
        else:
            cpuValueList.append(0)
            timeList.append(kontrol)
            kontrol += 1
        
        

    return timeList,cpuValueList

