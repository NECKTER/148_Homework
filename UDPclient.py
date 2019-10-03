from socket import *
server = 'localhost'
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)
message = open('testcases.txt', 'r').read()
client_socket.sendto(message.encode(), (server, server_port))
result, server_Addr = client_socket.recvfrom(2048)
print(result.decode())
client_socket.close()
