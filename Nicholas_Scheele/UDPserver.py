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


server_port = 12000                                             #port number
server_socket = socket(AF_INET, SOCK_DGRAM)                     #use SOCK_DGRAM for UDP
server_socket.bind(("", server_port))                           #define the port being used for comunication
print('UDP server is ready')
while True:
    message, client_Addr = server_socket.recvfrom(2048)         #recieve data from a client
    result_message = countBetweenSpace(message)                 #preform manipulation of data
    server_socket.sendto(result_message.encode(), client_Addr)  #return the result to the client

