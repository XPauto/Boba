import socket
import time
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# GLOBAL VARIABLES

IP = 'localhost'
PORT = 9999

client.connect((IP, PORT))
msg = client.recv(1024)

print("Boba!")
print("")
print(msg.decode('utf-8'))
print("")

while True:
    try:
        MSG = input("Store: ")
        FORMATMSG = MSG + " - " + str(time.asctime())
        client.send(MSG.encode('utf-8'))
    except ConnectionResetError:
        print("")
        print("Server has been shut-down! :(")
        client.close()
        sys.exit()
