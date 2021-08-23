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



if __name__ == "__main__":
    main()