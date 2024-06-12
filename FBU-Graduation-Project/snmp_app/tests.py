from django.test import TestCase
import sqlite3
from pythonping import ping
from pysnmp.hlapi import *





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

a = '192.168.1.11'[:'192.168.1.11'.rindex('.')]

print(a)