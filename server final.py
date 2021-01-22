# Save as server.py
# Message Receiver
def decrypt(data, key):
    alp = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    ans = []
    check = ''
    j = 0
    for i in data:
        if i == ' ':
            check = True
        if j == len(key):
            j = 0
        num = alp.index(i) - alp.index(key[j])
        if num >= len(alp):
            num = num + len(alp)
        ans.append(alp[num])
        j += 1
    return ans
count = 0
pass_count = 0
import getpass
import sys
import os
from socket import *
host = ""
port = 8080
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print("Waiting to receive messages...")
while True:
    while count < 1:
        count += 1
        (data, addr) = UDPSock.recvfrom(buf)
        key = data.decode('utf-8')
        if data == "exit":
            break
    while True:
        (data, addr) = UDPSock.recvfrom(buf)
        print("Received message: " + str(data))
        msg = data.decode('utf-8')
        final_msg = (decrypt(msg, key))
        while True:
            try:
                code = getpass.getpass("Enter password: ")
                if code == '8am35HAN':
                    print(''.join(final_msg))
                    break
            except:
                pass_count += 1
                print("Try Again")
        if data == "exit":
            break
UDPSock.close()
os._exit(0)
