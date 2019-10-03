from socket import *


def countBetweenSpace(message):
    i = 0
    result = ''
    for ch in message:
        if (chr(ch) == ' ') or (chr(ch) == '\n'):
            if chr(ch) == '\n':
                result += '\n'
            result += str(i) + ' '
            i = 0
        else:
            i += 1
    return result


server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(("", server_port))
print('UDP server is ready')
while True:
    message, client_Addr = server_socket.recvfrom(2048)
    result_message = countBetweenSpace(message)
    server_socket.sendto(result_message.encode(), client_Addr)

