import socket

import client
import server
import json

FILE_PATH = 'config.json'


def parse_config():
    config = json.load(open(FILE_PATH))
    return config["IP"], int(config["PORT"])


def main():

    usr = input("Send or receive? [S/R]?")

    ip, port = parse_config()
    if usr.upper() == "S":
        client.start(port, ip)
    elif usr.upper() == "R":
        server.start(port, socket.gethostbyname(socket.gethostname()))
    else:
        print("[ERROR] INCORRECT SEQUENCE")


if __name__ == "__main__":
    main()
