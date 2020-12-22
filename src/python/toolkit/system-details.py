import platform
import sys
import os
import psutil
import re
import uuid

uname = platform.uname()
architecture = platform.architecture()
python_version = platform.python_version()
system_architecture = "32 bits"
if (sys.maxsize > 2**32): system_architecture = "64 bits"
platformInfo = platform.platform().split("-")
system_edition = platform.win32_edition()
memory = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))

print()

print(f"System: {uname.system} {uname.release} {system_edition} {platformInfo[3]} {system_architecture} ")
print(f"Version: {uname.version} ")
print(f"Node name: {uname.node} ")
print(f"Machine: {uname.machine} ")
print(f"Processor: {uname.processor} ")
print(f"Memory: {memory}")
print()
print(f"MAC Address: {mac_address}")
print()
print(f"Login: {os.getlogin()}")
print()
print(f"Python version: {python_version} ")
#print(sys.copyright)
#windows_version = sys.getwindowsversion()
#print(windows_version)
#print(windows_version.service_pack_major)
print()

addrs = psutil.net_if_addrs()
print(addrs.keys())
print("==================")
print(addrs["Ethernet"])
print("==================")
print(addrs["Wi-Fi"])

print("==================")

for name, addrs in psutil.net_if_addrs().items():
    print(name)
    for addr in addrs:
        print(addr)

import socket
def network_status():
    interfaces = psutil.net_if_addrs()
    for name, addrs in interfaces.items():
        key = name
        status = { "name": name, "ipv4" : "-", "ipv6" : "-", "mac" : "-", "netmask": "" }
        
        for addr in addrs:
            #print(addr)
            if addr.family == socket.AF_INET: status["ipv4"] = addr.address
            if addr.family == socket.AF_INET6: status["ipv6"] = addr.address
            if addr.family == psutil.AF_LINK: status["mac"] = addr.address
            status["netmask"] = addr.netmask
        print(status)

network_status()