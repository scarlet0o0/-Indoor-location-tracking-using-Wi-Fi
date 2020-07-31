import os
import sys

spliiter = ' '

def fileparsing(value):
    
    dBm_list=[] 
    name_list=[]
    rt=[]
    
    for itr in value:
        if(itr.find('level=')!=-1):
            dBm=itr.split('level=')[1]
            dBm_list.append(str(dBm.split(' ')[0]))
        if(itr.find('ESSID:')!=-1):
            name=itr.split('ESSID:')[1]
            name_list.append(str(name[1:-2]))
    
    for num in range(len(name_list)):
        rt.append(name_list[num])
        rt.append(dBm_list[num])
    
    return rt
    

def send2server(value):
    import socket
    
    HOST='118.47.209.163'
    PORT=9999
    
    cilentSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    cilentSock.connect((HOST,PORT))
    
    cilentSock.sendall(value.encode())
    
    cilentSock.close()
    

def main(x,y,number):
    
    # my_command = "hello-"
    # my_fname = i + "-world"
    #complete_command = my_command + my_fname
    
    NameDBm_list=[]
    dBmMedian_list=[]
    
    for num in range(number):
        os.system("sudo iwlist wlan0 scan | grep -E 'level|ESSID'>wifiList.txt")
        wifi_f = open('wifiList.txt', 'r')
        lines = wifi_f.readlines()
        NameDBm_list.append(fileparsing(lines))
    val_list=fileparsing(lines)
    
    
    for num in range(len(val_list)//2):
        dBm_list=[]
        for num2 in range(number):
            dBm_list.append(NameDBm_list[num2][num*2+1])
            print(NameDBm_list[num2][num*2+1])
        dBm_list.sort()
        dBmMedian_list.append(dBm_list[number//2])
        
    for num in range(len(dBmMedian_list)):
        val_list[num*2+1]=dBmMedian_list[num]
    
    
    return_value=str(x)+spliiter+str(y)+spliiter+spliiter.join(val_list)
    
    send2server(return_value)

main(1,2,3)
#main(sys.argv[1],sys.argv[2],sys.argv[3])

    
    





