import socket
from urllib import response 

target_host = "0.0.0.0"
target_port = 9997

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(b"whoami")

repsonse = client.recv(4096)

print(response)
client.close()