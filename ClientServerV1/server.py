import socket
import subprocess

HOST = '127.0.0.1'
PORT = 50001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))
server_socket.listen()

conn,addr = server_socket.accept()
print("Connected from:"+str(addr))

while True:
    data = conn.recv(1024).decode()
    print(data)

    result = subprocess.run(data,stdout=subprocess.PIPE, shell=True)
    if(result.stdout.decode()!=""):
        response_data=result.stdout
    else:
        response_data=("Command Executed").encode()

    conn.send(response_data)
conn.close()