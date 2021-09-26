import socket
import base64
import os

DEFAULT_BUFFER_SIZE = 64
BYTE_ORDER = 'little'
ENCODING = 'utf-8'


# This function receives data from the client. It will use two calls to socket.recv: 1 for the buffer, the other for
# the data itself, returned as bytes
def recv_data(client: socket.socket) -> bytes:
    # obtain the buffer
    bufferBytes = client.recv(DEFAULT_BUFFER_SIZE)
    buffer = int.from_bytes(bufferBytes, BYTE_ORDER)

    # use the buffer to obtain what is really being sent
    return client.recv(buffer)

def handle_file(client: socket.socket, file):
    data = recv_data(client)
    os.write(file, base64.b64decode(data))
    while len(data) > 0:
        data = recv_data(client)
        os.write(file, base64.b64decode(data))
        print("Writing")

def handle_client(client: socket.socket) -> None:
    # get our file name from the client server
    fName = recv_data(client).decode(ENCODING)

    # create a file with the client file name
    file = os.open("/home/jake/Desktop/Testing/" + fName, os.O_RDWR | os.O_CREAT)

    handle_file(client, file)

    os.close(file)

def start(port, host: str) -> None:
    # create socket and bin6d to a port
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    print(f"[SERVER] LISTENING ON {host}:{port}")

    # listen and reject up to five connections
    server.listen(5)

    # accept the connection
    client, addr = server.accept()
    print(f"[SERVER] CONNECTION ESTABLISHED WITH {addr}")

    handle_client(client)

    client.close()
    server.close()
