from socket import *


#takes in the string that was sent to us by the client and steps through
#counting the characters on each line that are seperated by a space
def countBetweenSpace(message):
    i = 0
    result = ''
    for ch in message:
        if (chr(ch) == ' ') or (chr(ch) == '\n'):
            result += str(i) + ' '
            i = 0
            if chr(ch) == '\n':
                result += '\n'
        else:
            i += 1
    if i > 0:
        result += str(i)
    return result


server_port = 12000                                     #port number
server_socket = socket(AF_INET, SOCK_STREAM)            #use SOCK_STREAM for TCP
server_socket.bind(('', server_port))                   #define the port being used for comunication
server_socket.listen(1)                                 #open port
print('server is listening and ready to receive')
while True:
    connection_socket, addr = server_socket.accept()    #connect to client

    sentence = connection_socket.recv(1024)             #recieve data
    result_message = countBetweenSpace(sentence)        #preform manipulation of data
    connection_socket.send(result_message.encode())     #return the result to the client

    connection_socket.close()                           #end communication with client
