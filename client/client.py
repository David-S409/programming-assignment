#! /usr/bin/env python3
import ftplib
import os
from client_cli_setup import setup_cli


def write_callback(data):
    global total_bytes
    total_bytes += len(data)
    print(f"Transferred {len(data)} bytes. Total transferred: {total_bytes} bytes.")
    f.write(data)


def send_callback(data):
    global total_bytes
    total_bytes += len(data)
    print(f"Transferred {len(data)} bytes. Total transferred: {total_bytes} bytes.")


# connect to FTP server
ftp = ftplib.FTP(host="0.0.0.0")
ftp.login(user="user", passwd="password")
ftp.sendcmd("TYPE i")
done = False

while not done:
    input_str = input("ftp>> ")
    cmd = input_str.split()

    match cmd[0].upper():
        case "GET":
            files = ftp.nlst()
            if len(cmd) >= 2:
                if cmd[1] not in files:
                    print("File does not exist")
                    continue
                total_bytes = 0
                # # download file
                with open("./data/" + cmd[1], "wb") as f:
                    result = ftp.retrbinary(
                        "RETR " + cmd[1], blocksize=1024, callback=write_callback
                    )
                print(cmd[1] + " was transferred successfully!")
            else:
                print("Please specify a file name")
        case "PUT":
            if os.path.exists("./data/" + cmd[1]):
                total_bytes = 0
                with open("./data/" + cmd[1], "rb") as f:
                    ftp.storbinary(
                        "STOR " + cmd[1], f, blocksize=1024, callback=send_callback
                    )
                print(cmd[1] + " was transferred successfully!")

            else:
                print("File not found to upload.")
        case "LS":
            ftp.dir()

        case "QUIT":
            ftp.quit()
            print("Disconnected from FTP Server")
            done = True
        case _:
            print("Unknown Command")
