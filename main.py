import client
import server
import json

FILE_PATH = 'config.json'


def parse_config():
    config = json.load(open(FILE_PATH))
    return config["IP"], config["PORT"]


def main():

    print("Send or receive? [S/R]?")
    usr = input()
    ip, port = parse_config()
    if usr == "S":
        client.start(port, ip)
    elif usr == "R":
        server.start(port, ip)
    else:
        print("[ERROR] INCORRECT SEQUENCE")


if __name__ == "__main__":
    main()
