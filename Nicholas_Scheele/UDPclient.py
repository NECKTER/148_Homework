from socket import *


server = 'localhost'                                            #server ip
server_port = 12000                                             #server port number
client_socket = socket(AF_INET, SOCK_DGRAM)                     #UDP connection using DGRAM
message = open('testcases.txt', 'r').read()                     #get data from local file
client_socket.sendto(message.encode(), (server, server_port))   #send data to server
result, server_Addr = client_socket.recvfrom(2048)              #wait for server reply
print(result.decode())                                          #print result
client_socket.close()                                           #end connection
