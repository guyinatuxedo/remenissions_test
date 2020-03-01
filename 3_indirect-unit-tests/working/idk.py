from pwn import *

from functools import wraps
import errno
import os
import signal
import time
import argparse
import pickle

hexChars = [0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66]
def parse0xInfoleak(string):
	startIndex = string.find("0x")

	stringLen = len(string)
	index = startIndex + 2
	foundEnd = False
	while foundEnd == False:

		if string[index] in hexChars:
			#print(string[index])
			index = index + 1
			if index >= (stringLen - 1):
				foundEnd = True


	hexString = string[startIndex:index + 1]
	hexValue = int(hexString, 16)

	preceedingString = string[:startIndex]
	proceedingString = string[index]
	return [preceedingString, proceedingString, hexValue]


def parse0x(string):
	startIndex = string.find("0x")

	stringLen = len(string)
	index = startIndex + 2
	foundEnd = False
	while foundEnd == False:

		if ord(string[index]) in hexChars:
			#print(string[index])
			index = index + 1
			if index >= (stringLen - 1):
				foundEnd = True
		else:
			#print("end found")
			#print(string[index])
			foundEnd = True

	hexString = string[startIndex:index + 1]

	#print("dance with the devil: %s" % str(hexString))
	hexValue = int(hexString, 16)

	return hexValue

def doesStringHaveNumbers(string):
	for char in string:
		if char.isdigit():
			return True
	return False

def adjustMemRegion(memRegion, areaStart, areaEnd):
	if memRegion["start"] > areaStart:
		memRegion["start"] = areaStart
	if memRegion["end"] < areaEnd:
		memRegion["end"] = areaEnd

stack = {"start": 0xffffffffffffffff, "end": 0x0, "region": "stack"}
libc  = {"start": 0xffffffffffffffff, "end": 0x0, "region": "libc"}
pie   = {"start": 0xffffffffffffffff, "end": 0x0, "region": "pie"}
memRegions = {"stack": stack, "libc": libc, "pie": pie}

def queryMemoryRegions():

	target.sendline("vmmap")
	memMappings = target.recvuntil("gef").split("\n")[2:-1]
	#print("live as")
	for line in memMappings:
		lineParts = line.split(" ")
		if "stack" in lineParts[4]:
			areaStart = int(lineParts[0], 16)
			areaEnd   = int(lineParts[1], 16)
			adjustMemRegion(stack, areaStart, areaEnd)
		if "libc" in lineParts[4]:
			areaStart = int(lineParts[0], 16)
			areaEnd   = int(lineParts[1], 16)
			adjustMemRegion(libc, areaStart, areaEnd)

		if targetBinary in lineParts[4]:
			areaStart = int(lineParts[0], 16)
			areaEnd   = int(lineParts[1], 16)
			adjustMemRegion(pie, areaStart, areaEnd)

		#print(lineParts)
	#print("you die")

def processInfoleak(infoleak):
	for memRegion in memRegions.values():
		if (infoleak >= memRegion["start"]) and (infoleak <= memRegion["end"]):
			region = memRegion["region"]
			offset = infoleak - memRegion["start"]
			return [region, offset]
	return None

def reportInfoleak(infoleak):
	print("Infoleak is: %s" % str(infoleak))

def convertHexStringToString(inputString):
	if type(inputString) == str:
		inputString = inputString.strip("0x").strip("\n")
		if len(inputString) < 16:
			inputString = "0"*(16 - len(inputString)) + inputString
		for i in range(0, (len(inputString) / 2)):
			currentByte = "0x" + inputString[(i*2)] + inputString[(i*2) + 1]
			currentByte = int("0x%s" % currentByte, 16)

def getReturnAddress():
	target.sendline("info frame")
	frameOutput = target.recvuntil("gef").split("\n")
	for line in frameOutput:
		if "saved rip" in line:	
			returnAddress = line.split("saved rip = ")[1]
			returnAddress = parse0x(returnAddress)
			return returnAddress

def isMappedMemory(address):
	if ((address >= libc["start"]) and (address <= libc["end"])) or ((address >= stack["start"]) and (address <= stack["end"])) or ((address >= pie["start"]) and (address <= pie["end"])):
		return True
	return False

def isValueFromInput(value):
	global inputs

	isFromInput = False
	whichInput 	= False
	offset		= False

	string = None



	if (type(value) == int) or (type(value) == long):
		string = intToString(value)

	if type(string) == str:
		string = string.strip("\n")


	if string == None:
		return isFromInput, whichInput, offset

	for i in range(0, len(inputs)):
		if string in inputs[i]:
			isFromInput = True
			whichInput = i
			offset = inputs[i].index(string)

	return isFromInput, whichInput, offset



def intToString(value):
	hexString = hex(value)[2:]
	if len(hexString) % 2 != 00:
		hexString = "0" + hexString
	string = ""
	for i in range(0, (len(hexString) / 2)):
		currentByte = "0x" + hexString[(i*2)] + hexString[(i*2) + 1]
		string += chr(int(currentByte, 16))
	return string

def reverseInt(value):



	returnValue = 0x00
	for i in range(0, 8):
		currentByte = ((value & (0xff << (i*8))) >> (i*8))
		returnValue = returnValue | (currentByte << ((7 - i)*8))

	return returnValue

def reportBufferOverflow(offset):
	global bugFound
	print("Reporting overflow")

	function = None

	address = None
	callingFunction = None
	overwriteableValues = [offset, "return_address"]
	additionalCmps = []
	indirectCalls = []
	bofBug = ["stack", function, callingFunction, address, overwriteableValues, additionalCmps, indirectCalls]
	bugFound = True

	if outputFile != None:
		print("dumping")
		#if os.path.exists(outputFule):
		#	output = open(outputFile, "a")
		#else:
		output = open(outputFile, "w")
		pickle.dump(bofBug, output)
		output.close()	

	print("\n\nBefore the blow to the head: %s\n\n" % str(bofBug))
	#sys.exit(0)

def gotCrash():
        print("y0")
	returnAddress = getReturnAddress()
	if (isMappedMemory(returnAddress) == False):
                print("y0 y0")
		reveresedReturnAddress = reverseInt(returnAddress)
		isFromInput, whichInput, offset = isValueFromInput(reveresedReturnAddress)
		if isFromInput != False:
                        print("y0 y0 y0")
			reportBufferOverflow(offset)
	target.interactive()
	sys.exit()

'''
def isAddressInCurrentStack():
	target.sendline("p $rbp")
	print("hello %s: " % rbp)
'''
def processOutput(output):
	outputLen = len(output)
	if outputLen == 0:
		return

	if "SIGSEGV" in output:
		gotCrash()

	if "exited" in output:
		return


	hasNumber = doesStringHaveNumbers(output)
	if hasNumber == False:
		return
'''
	infoleak = None
	if "0x" in output:
		parsedInfoleak = parse0xInfoleak(output)
		queryMemoryRegions()
		infoleak = processInfoleak(parsedInfoleak[2])

	if infoleak != None:
		if infoleak[0] == "stack":
			print("stack infoleak yo")
			#isAddressInCurrentStack()
			#target.interactive()
		reportInfoleak(infoleak)
'''

class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator

@timeout(1)
def hi():
    try:
        x = target.recvuntil("gef").split("\n\nThat's what")[0].split("Continuing.\n")[1]
        return x
    except:
        return False




def setup():
	global target
	global targetBinary

	target = process(["gdb", ("./%s" % targetBinary)])

	target.recvuntil("gef")

	target.sendline("catch syscall read write")

	#target.sendline("catch syscall write")

	target.recvuntil("gef")

	target.sendline("commands")

	target.sendline("silent")

	target.sendline("echo \\n\\nThat's what you do best\\n\\n")

	target.sendline("end")

	target.recvuntil("gef")

	target.sendline("r")
	target.recvuntil("gef")
	target.recvuntil("gef")
	target.recvuntil("gef")
	x = target.recvuntil("gef").split("\n\nThat's what")

	target.sendline("c")




'''
while "exited normally" not in x:
	if exited == True:
		print("yo")
		sys.exit(0)
	while x != False:
		if ("exited normally" in x) or ("not being run" in x):
			print("yo")
			sys.exit(0)
		processOutput(x)
		target.sendline("c")
		x = hi()

	target.sendline("15935728")
	target.sendline("c")
	x = hi()
	if x == False:
		exited = True
'''
firstByte = 0x21
secondByte = 0x21
inputs = []

# Just saying, this is totally based off of gefs pattern create functionallity
def genInput(inputSize):
	global firstByte
	global secondByte
	global inputs

	currentSize = 0
	currentInput = ""
	while currentSize != inputSize:
		if currentSize < inputSize:
			currentInput += chr(firstByte)*7 + chr(secondByte)
			firstByte, secondByte = incrementBytes(firstByte, secondByte)
			currentSize += 8

		elif currentSize > inputSize:
			offset = currentSize - inputSize
			currentInput = currentInput[0:-offset]
			currentSize = inputSize

	return currentInput



def incrementBytes(firstByte, secondByte):
	maxByte = 0x7e
	minByte = 0x21

	secondByte = secondByte + 1
	if secondByte >= maxByte:
		secondByte = minByte
		firstByte += 1

	return firstByte, secondByte

def sendInput():
	targetInput = genInput(5000)
	inputs.append(targetInput)
	target.sendline(targetInput)



def mainLoop():
	#target.interactive()
	#x = target.recvuntil("gef")
	#while "That's what" not in x:
	#	target.sendline("c")
	#	x = target.recvuntil("gef")
	x = target.recvuntil("gef").split("\n\nThat's what")[0].split("Continuing.\n")[1]
	#x = target.recvuntil("gef").split("\n\nThat's what")[0].split("Continuing.\n")[1]
	exited = False
	#target.interactive()
	while exited == False:	
		while x != False:
			if ("exited normally" in x) or ("not being run" in x):
				print("yo")
				sys.exit(0)
			processOutput(x)
			target.sendline("c")
			x = hi()

		sendInput()
		target.sendline("c")

		x = hi()
		if x == False:
			exited = True
	print("yo")



bugFound = False
def mainCaller(recursionDepth):
	global bugFound
	print("\n\nDepth is: %d\n\n" % recursionDepth)
	if recursionDepth > 5 or bugFound == True:
		return

	try:
        #if 1 == 1:
		setup()
		mainLoop()
	except:
		if bugFound == False:
			mainCaller(recursionDepth + 1)

def helpFunction():
	print("Get Good")
	sys.exit(0)



if __name__ == "__main__":
	global targetBinary
	global target
	parser = argparse.ArgumentParser(description = "Anaylzer for binaries using gdb")
	parser.add_argument("-b", metavar="-B", type=str, help="The Bianry to analyze", default = None)
	parser.add_argument("-o", metavar="-O", type=str, help="The output file", default = None)

	args = parser.parse_args()

	targetBinary	= args.b
	outputFile 		= args.o

	if targetBinary == None:
		helpFunction()

	mainCaller(0)

targetBinary = "hi"
outputFile = None
target = None
