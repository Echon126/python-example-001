import re
import os
#
# subject = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7625A5220006010A01AAAAAAAAAAAAAAAA2E00AE0B,AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7625A5220006010A02AAAAAAAAAAAAAAAA2E03E692,AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7625A5220006010A09AAAAAAAAAAAAAAAA2E088D8D"
# strs = subject.split(",")
# for str in strs:
#     result = re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", str)
#     print(result)


def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False


def writeText():
    try:
        with  open("E:\\xxxxx\\xxxxxx.txt", 'a', encoding='utf-8') as f:
            f.write("zzzzzzzzzzzzzzzzz")
    except IOError:
        print("this is data error ")
    else:
        print("file write success")
        f.close()


import socket


def SocketStart():
    server = socket.socket()
    ip_port = ("192.168.140.89", 60000)
    server.bind(ip_port)
    server.listen()
    conn, addr = server.accept()
    print(conn.recv(1024).decode())
    print(addr)


if __name__ == "__main__":
    # mkdir("E:\\xxxxx\\")
    # writeText()
    SocketStart()
