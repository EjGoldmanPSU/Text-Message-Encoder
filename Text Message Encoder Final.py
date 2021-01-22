#Create program that send messages then encrypts them
#Once user enter fingerprint or password show decrypted message
import random
import string
alp = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))
def encrypt(phrase, key):
       check = ''
       ans = []
       j = 0
       for i in phrase:
              if i == ' ':
                     check = True
              if j == len(key):
                     j = 0
              num = alp.index(i) + alp.index(key[j])
              if num >= len(alp):
                     num = num - len(alp)
              ans.append(alp[num])
              j += 1
       msg = ''
       for i in ans:
              msg += i
       return msg
count = 0
while True:
       while count < 1:
              count += 1
              key = random_char(10).lower()
              import os
              from socket import *
              host = "100.64.13.248" # set to IP address of target computer
              port = 8080
              addr = (host, port)
              UDPSock = socket(AF_INET, SOCK_DGRAM)
              while True:
                     data  = key.encode('utf-8')
                     UDPSock.sendto(data, addr)
                     break
              while True:
                     phrase = input('Enter Message --> ')
                     e = encrypt(phrase.lower(), key)
                     import os
                     from socket import *
                     host = "100.64.13.248" # set to IP address of target computer
                     port = 8080
                     addr = (host, port)
                     UDPSock = socket(AF_INET, SOCK_DGRAM)
                     while True:
                         data  = e.encode('utf-8')
                         UDPSock.sendto(data, addr)
                         break
