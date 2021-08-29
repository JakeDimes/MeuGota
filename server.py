import socket
import base64
import os

def handle_file(client: socket.socket) -> str:

    fTemp = os.open("~/Desktop/Testing/test.txt", 'wb')

    buffer = int.from_bytes(client.recv(64), 'little')
    fileBytes = client.recv(buffer)
    file = base64.b64decode(fileBytes)
    os.write(fTemp, file)


def start(port, host: str):

    # create socket and bin6d to a port
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    print(f"[SERVER] LISTENING ON {host}:{port}")

    # listen and reject up to five connections
    server.listen(5)

    # accept the connection
    client, addr = server.accept()
    print(f"[SERVER] CONNECTION ESTABLISHED WITH {addr}")
    handle_file(client)

    client.close()
    server.close()
