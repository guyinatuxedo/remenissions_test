from pwn import *

target = process(["gdb", "./hi"])

target.recvuntil("gef")

target.sendline("catch syscall read")

target.recvuntil("gef")

target.sendline("commands")

target.sendline("silent")

target.sendline("echo \\n\\nThat's what you do best\\n\\n")

target.sendline("end")

target.recvuntil("gef")

target.sendline("r")
target.recvuntil("gef")
target.recvuntil("gef")
target.recvuntil("gef")
x = target.recvuntil("gef").split("\n\nThat's what")

target.sendline("c")

x = target.recvuntil("gef").split("\n\nThat's what")[0].split("Continuing.\n")[1]

while x == "":
	print("\n\nX is: %s\n\n" % str(x))
	target.sendline("c")
	x = target.recvuntil("gef").split("\n\nThat's what")[0].split("Continuing.\n")[1]


target.sendline("c")

target.sendline("15935728")


print("\n\n\nkeep it away: %s\n\n\n" % str(x))


target.interactive()