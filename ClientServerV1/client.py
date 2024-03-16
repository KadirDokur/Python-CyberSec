import socket

HOST = '127.0.0.1'
PORT = 50001

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))

message = input(">>  ")

while (message.lower().strip()!="quit"):
    if(message!=""):
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(("Response from Server : "+str(data)))
    message = input(">>  ")
