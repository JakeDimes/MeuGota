import socket
import base64
import os

DEFAULT_BUFFER_SIZE = 64
BYTE_ORDER = 'little'
ENCODING = 'utf-8'
FILE_READ_SIZE = 4096

# this function sends data to the server socket. It will calculate a buffer and send the 'data' variable
def send_data(client: socket.socket, data: bytes):

    buffer = len(data)
    client.send(buffer.to_bytes(DEFAULT_BUFFER_SIZE, BYTE_ORDER))
    client.send(data)

def send_file(client: socket.socket, file) -> None:

    fileBytes = os.read(file, FILE_READ_SIZE)
    send_data(client, base64.b64encode(fileBytes))

    while len(fileBytes) > 0:
        fileBytes = os.read(file, FILE_READ_SIZE)

        send_data(client, base64.b64encode(fileBytes))


# gets the file name from the file import string
def get_file_name(path: str) -> str:

    startIndex = path.rfind(os.sep) + 1
    return path[startIndex:]


# this serves as the 'main method' for handling the file(s) the client wishes to send
def file_handle(client: socket.socket):
    # obtain the path for the file
    fpath = input("Enter file path: ")

    # get file name (and extension)
    fname = get_file_name(fpath)
    print(f"[CLIENT]: FILE NAME IS: {fname}")

    # read binary file
    file = os.open(fpath, os.O_RDONLY)

    # send file name to server
    send_data(client, fname.encode(ENCODING))

    # send the file to server
    send_file(client, file)


# this serves as the 'main method' for the client socket
def start(port, host: str):
    # create client socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect
    print(f"[CLIENT] ATTEMPTING TO CONNECT TO: {host}:{port}")
    client.connect((host, port))

    print(f"[CLIENT]: CONNECTION TO {host} SUCCESSFUL")

    file_handle(client)

    client.close()
