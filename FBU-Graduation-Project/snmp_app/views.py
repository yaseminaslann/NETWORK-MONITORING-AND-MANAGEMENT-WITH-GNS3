import datetime
from pythonping import ping
from django.shortcuts import render
from pysnmp.hlapi import *
from netmiko import ConnectHandler
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import sys
from django.contrib.sessions.models import Session
import sqlite3
from . import customScripts


def get_snmp_data(oid, ip):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData('public', mpModel=1),  # SNMPv2c
        UdpTransportTarget((ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(f"Error: {errorIndication}")
        return 'Erişim Yok'
    elif errorStatus:
        print(f"Error: {errorStatus.prettyPrint()}")
        return 'Erişim Yok'
    else:
        for varBind in varBinds:
            return varBind.prettyPrint().split(' = ')[1]
    return None

def get_netmiko_data(ip, username, password, command):
    try:
        device = {
                'device_type': 'cisco_ios',
                'host': f'{ip}',
                'username': f'{username}',
                'password': f'{password}',
        }
        connection = ConnectHandler(**device)
        output = connection.send_command(command)
        connection.disconnect()
        return output
        
    except Exception as e:
        return str(e)

def index(request):

    deviceList = customScripts.getDataDB()

    contextList = []

    ipaddrList = []

    for device in deviceList:

        upCheck = ping(device['ip'], timeout=0.2)
        if 'Reply' in str(upCheck):
            contextList.append({
                'db_ip': device['ip'],
                'ip_address': get_snmp_data(ip=device['ip'],oid=f".1.3.6.1.2.1.4.20.1.1.{device['ip']}"),
                'netmask': get_netmiko_data(ip=device['ip'], username=device['username'], password=device['password'], command='sh run | inc 255').split(' ')[-1],
                'cpu_usage': get_netmiko_data(ip=device['ip'], username=device['username'], password=device['password'], command='show processes cpu | include one minute'),
                'hostname': get_netmiko_data(ip=device['ip'], username=device['username'], password=device['password'], command='show version | include IOS'),
                'clock': get_netmiko_data(ip=device['ip'], username=device['username'], password=device['password'], command='show clock'),
                'uptime': get_netmiko_data(ip=device['ip'], username=device['username'], password=device['password'], command='show version | include uptime'),                   
            })

            ipaddrList.append(device['ip'])
        else:
            contextList.append({
                'db_ip': device['ip'],
                'ip_address': 'Erişim Yok',
                'netmask': 'Erişim Yok',
                'cpu_usage': 'Erişim Yok',
                'hostname': 'Erişim Yok',
                'clock': 'Erişim Yok',
                'uptime': 'Erişim Yok',                   
            })

            ipaddrList.append(device['ip'])



    labels, data = customScripts.getCPUValue(ip=device['ip'],username=device['username'], password=device['password'])

    ChartData = {
        'ipaddr': ipaddrList,
        'labels': labels,
        'data': data,
    }
    return render(request, 'snmp_app/index.html', context={'deviceList':contextList,'context':ChartData})

def userlogin(request):
    if request.method == "POST":
        userName = request.POST['name']
        userPass = request.POST['psw']
        user = authenticate(username=f'{userName}', password=f'{userPass}')

        if user is not None:
            login(request, user)
            # set user-specific data in the session
            request.session['username'] = userName
            request.session.save()
            return index(request)
        else:
            return render(request,'snmp_app/error.html', context={'message':'Hatalı Kullanıcı'})
    return render(request,'snmp_app/login.html')

def register(request):
    if request.method == "POST":
        userName = request.POST['name']
        userEmail = request.POST['email']
        userLastName = request.POST['lastname']
        userPass = request.POST['psw']
        user = User.objects.create_user(username=f'{userName}',email=f'{userEmail}', password=f'{userPass}')
        user.last_name = f'{userLastName}'
        user.save()
        return index(request)

    return render(request,'snmp_app/register.html')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        Session.objects.filter(session_key=request.session.session_key).delete()
        return index(request)
        

def devicelist(request):
    print(request.POST)
    if request.method == 'POST':
        if 'command' in dict(request.POST):
            outputList = []
            for ip in dict(request.POST)['ip']:
                dbconnect = sqlite3.connect('device.sqlite3')
                dbcursor = dbconnect.cursor()

                password = customScripts.getQueryOneOutput(f"SELECT Password from Device WHERE IP='{request.POST['ip']}'")
                username = customScripts.getQueryOneOutput(f"SELECT User from Device WHERE IP='{request.POST['ip']}'")


                command = request.POST['command']



                print(ip)
                output = get_netmiko_data(ip=ip, username=username, password=password, command=command)


                outputList.append({'ip':ip,'output':output})
            return render(request,'snmp_app/output.html', context={'outputDevices':outputList})

        elif 'newdevicepass'in request.POST:
            ip = request.POST['newdeviceip']
            username = request.POST['newdeviceuser']
            password = request.POST['newdevicepass']

            dbconnect = sqlite3.connect('device.sqlite3')
            dbcursor = dbconnect.cursor()
            dbcursor.execute(f"INSERT INTO Device(IP,User,Password) VALUES ('{ip}', '{username}', '{password}')")
            dbconnect.commit()
            dbconnect.close()
            return index(request)
    else:
        deviceList = customScripts.getDataDB()
        return render(request,'snmp_app/deviceList.html', context={'deviceList': deviceList})


