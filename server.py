import socket

HOST = '118.47.209.163'
PORT = 9999        

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

client_socket, addr = server_socket.accept()
print('Connected by', addr)

data = client_socket.recv(1024)

rt=data.decode()

wifilist=rt.split(" ")

for num in range(1,len(wifilist)):
    if(num==1):
        print("x:"+wifilist[0])
        print("y:"+wifilist[1])  
    elif(num%2==0):
        print("wifi:"+wifilist[num])
    else:
        print("dBm:"+wifilist[num])

client_socket.close()
server_socket.close()










