from pwn import *

import time

import sys

target = process("./chall-test_nctf19-babypwn")
gdb.attach(target, gdbscript="get_libc_puts_address")

