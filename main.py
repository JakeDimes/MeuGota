import client
import server

def main():
    print("Send or receive? [S/R]?")
    usr = input()
    if usr == "S":
        client.start()
    elif usr == "R":
        server.start()
    else:
        print("[ERROR] INCORRECT SEQUENCE")


if __name__ == "__main__":
    main()
