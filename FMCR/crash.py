#!/usr/bin/python3
from pwn import *

buffer = b"A" * 5000

data =  buffer 

print("[+]Length Buffer: " + str(len(buffer)))
print(data)