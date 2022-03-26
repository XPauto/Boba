import socket
from this import d
import time
import sys
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# GLOBAL VARIABLES

IP = 'localhost'
PORT = 9999
MAX_USERS = input("Max Connections: ")
MSG = ""
# MODE = input("Data Mode - (1) or Announcement Mode - (2)")
DATA = []

server.bind((IP, PORT))

# LISTEN FOR INCOMING CONNECTIONS

server.listen(10)

# LISTEN FOR STORAGE

def add_data():
    while True:
        MSG = conn.recv(1024)
        DATA.append(MSG.decode('utf-8'))
        print(DATA)

# MAIN LOOP

while True:
    try:
        conn, addr = server.accept()
        MSG = "Current Max Connections: " + MAX_USERS
        conn.send(MSG.encode('utf-8'))

        t = Thread(target=add_data)
        # # make the thread daemon so it ends whenever the main thread ends
        t.daemon = True
        # start the thread
        t.start()

        # elif MODE == "2":
        #     MSG = input("Send Announcement: ")
        #     FORMATMSG = "Announcement: " + MSG + " - " + str(time.asctime())
        #     conn.send(FORMATMSG.encode('utf-8'))
        #     # time.sleep(1)

    except ConnectionResetError:
        # CLOSE SERVER WHEN ALL USERS LEAVE

        print("All Users Have Left. :(")
        server.close()
        sys.exit()
