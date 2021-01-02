from os import name
import subprocess
import csv
from win32com.client import GetObject

def installed_package():
    lst = []
    lst = subprocess.run("C:\\Windows\\System32\\wbem\\WMIC.exe product get name",shell=True,text=True,capture_output=True)
    #lst = subprocess.run("dir",shell=True,capture_output=True,text=True)
    global com_list
    com_list = []
    for i in lst.stdout.split("\n\n"):
        com_list.append(i)
    com_list.pop(0)
    #return(com_list)
    with open('install_pack.csv', mode='w') as install_pack:
        install_pack_writer = csv.writer(install_pack, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        install_pack_writer.writerow(["Pakages Insatlled"])
        for n in com_list:
            install_pack_writer.writerow([n])
        '''
        for n in range(0,(len(com_list)+1),2):
            install_pack_writer.writerow([com_list[n],com_list[n+1]])
        for i in range(1,(len(com_list)+1),2):
             install_pack_writer.writerow([com_list[i],com_list[i+1]])    
        '''
def antivirus():
    objWMI = GetObject('winmgmts:\\\\.\\root\\SecurityCenter2').InstancesOf('AntiVirusProduct')
    with open('antivirus.csv', mode='w') as antivirus_lst:
        antivirus_lst_writer = csv.writer(antivirus_lst, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        antivirus_lst_writer.writerow(["Name","State","Version"])
        for obj in objWMI:
            hexing = hex(obj.productState)
            status = hexing[3:5]
            if status == '10':
                status = 'Running'
            else:
                status = 'Not Enabled'
            update = hexing[5:]
            if update == '00':
                update = "Latest"
            else:
                update = "Required Update"
            antivirus_lst_writer.writerow([str(obj.displayName),status,update])
    
def main():
    installed_package()
    antivirus()

if __name__ == '__main__':
    main()