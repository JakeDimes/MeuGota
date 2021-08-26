import socket


def handle(client: socket.socket) -> str:
    buffer = int.from_bytes(client.recv(64), 'little')
    return client.recv(buffer).decode('utf-8')


def start(port, host: str):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    print(f"[SERVER] LISTENING ON {host}:{port}")

    server.listen(5)

    client, addr = server.accept()
    print(f"[SERVER] CONNECTION ESTABLISHED WITH {addr}")
    print(f"[MSG] {handle(client)}")

    server.close()
