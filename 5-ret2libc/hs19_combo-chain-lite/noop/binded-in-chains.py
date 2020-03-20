from pwn import *

import time

import sys

target = process("./chall-test_combo-chain-lite")
gdb.attach(target, gdbscript="get_libc_puts_address")

