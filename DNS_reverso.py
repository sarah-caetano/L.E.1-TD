import socket

L = int(input())

for i in range (L):
    ip = input()
    dn = socket.gethostbyaddr(ip)
    print(dn[0])
