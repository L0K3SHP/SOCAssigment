import socket
import subprocess
import csv
import re

global up
global down  
up =[]
down = []

def status():
    if len(up) > 1:
        return("Up")
    elif len(down) >= 1:
        return("Down")

def ip_addr():
    global ip
    global hostname
    hostname = socket.gethostname()
    ip = socket.gethostbyname_ex(hostname)
    #print(f"Hostname: {ip[0]} \nIp Address: {ip[2]}")
    for i in ip[2]:
        if '127.0.0.1' in i:
            down.append('1')
            pass
        if len(down) == 0:
            ping = subprocess.call(['ping', f'{i}',],shell=False)
            if ping == 0:
                up.append(f'{i}')
            else:
                down.append(f'{i}')
    return ip

def main():
    ip_addr()
    status()
    with open('ip_hostname.csv', mode='w') as ip_hostname:
        ip_hostname_writer = csv.writer(ip_hostname, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        ip_hostname_writer.writerow(["Hostname", "Ip-Address","Status"])
        ip_hostname_writer.writerow([ip[0], ip[2],status()])
    
if __name__=='__main__':
    main()

