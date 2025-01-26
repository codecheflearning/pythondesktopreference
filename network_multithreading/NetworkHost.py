import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 4056))
serversocket.listen()

connection, address = serversocket.accept()
while True:
    buf = connection.recv(128)
    message = buf.decode()

    if message.lower() != 'bye':
        print(message)
    else:
        connection.send("bye".encode())
        print("Connection closed!")
        break

connection.close()
serversocket.close()
