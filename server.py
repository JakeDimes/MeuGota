import socket


def handle(client: socket.socket) -> str:
    buffer = int.from_bytes(client.recv(64), 'little')
    return client.recv(buffer).decode('utf-8')


def start(port, host: str):

    # create socket and bind to a port
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    print(f"[SERVER] LISTENING ON {host}:{port}")

    # listen and reject up to five connections
    server.listen(5)

    # accept the connection
    client, addr = server.accept()
    print(f"[SERVER] CONNECTION ESTABLISHED WITH {addr}")
    print(f"[MSG] {handle(client)}")

    client.close()
    server.close()
