import socket
import base64

def file_handle(client: socket.socket):
    print("Enter file path:")
    fpath = input("PATH: ")

    # read binary file
    file = open(fpath, 'rb')
    fileBytes = base64.b64encode(file.read())

    buffer = len(fileBytes)
    client.send(buffer.to_bytes(64, 'little'))
    client.send(fileBytes)


def start(port, host: str):
    # create client socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect
    print(f"[CLIENT] ATTEMPTING TO CONNECT TO: {host}:{port}")
    client.connect((host, port))

    print(f"[CLIENT]: CONNECTION TO {host} SUCCESSFUL")
    file_handle(client)

    client.close()
