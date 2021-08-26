import socket


def msg_proto(client: socket.socket, msg: str):
    buffer = len(msg).to_bytes(64, 'little', signed=False)
    client.send(buffer)
    client.send(msg.encode('utf-8'))


def start(port, host: str):
    # create client socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect
    print(f"[CLIENT] ATTEMPTING TO CONNECT TO: {host}:{port}")
    client.connect((host, port))

    print(f"[CLIENT]: CONNECTION TO {host} SUCCESSFUL")
    print("Enter message: ")
    msg = input()

    msg_proto(client, msg)
    client.close()
