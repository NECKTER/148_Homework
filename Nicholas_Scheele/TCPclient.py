from socket import *


server_name = 'localhost'                           #server ip
server_port = 12000                                 #server port number
client_socket = socket(AF_INET, SOCK_STREAM)        #UDP connection using STREAM
client_socket.connect((server_name, server_port))   #connect to the server
sentence = open('testcases.txt', 'r').read()        #get data from local file
client_socket.send(sentence.encode())               #send data to server
modified_sentence = client_socket.recv(1024)        #wait for server reply
print(modified_sentence.decode())                   #print result
client_socket.close()                               #end connection
