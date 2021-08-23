import socket

def handle(client: socket.socket):
    server.

def start(port, host: str):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))

    server.listen(5)

    client, addr = server.accept()
    print(f"[SERVER] CONNECTION ESTABLISHED WITH {addr}")
    server.close()