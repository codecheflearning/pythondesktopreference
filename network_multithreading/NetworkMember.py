import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 4056))

while True:
    # Client message
    message = input("Message: ")
    clientsocket.send(message.encode())
    if message.lower() == 'bye':
        server_response = clientsocket.recv(128)
        message = server_response.decode()
        print("Host says:" + message)
        print("Connection closed!")
        break

clientsocket.close()