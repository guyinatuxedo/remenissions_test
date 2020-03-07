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

def isHexAsciiCharacter(char):
	char = ord(char)
	if (char >= 0x30) and (char <= 0x39):
		return True

	elif (char >= 0x41) and (char <= 0x46):
		return True

	elif (char >= 0x61) and (char <= 0x66):
		return True

	return False

def doesStringHaveNumbers(string):
	for i in range(0, len(string)):
		if isHexAsciiCharacter(string[i]) == True:
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
	memMappings = target.recvuntil("gefffffffff").split("\n")[2:-1]
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
	frameOutput = target.recvuntil("gefffffffff").split("\n")
	for line in frameOutput:
		if "saved rip" in line:	
			returnAddress = line.split("saved rip = ")[1]
			returnAddress = parse0x(returnAddress)
			return returnAddress

def getReturnAddressAddress():
	target.sendline("info frame")
	frameOutput = target.recvuntil("gefffffffff").split("\n")
	for line in frameOutput:
		if "rip at" in line:	
			returnAddress = line.split("rip at ")[1]
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
	global reportBugs
	global bugFound

	if reportBugs == True:
		return



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

def getStringsBeforeAfter(string):
	global savedOutputs
	print("the dark before the dawn")
	index = savedOutputs.index(string)

	foundBeginning = False
	beforeString = ""
	while (index > -1) and foundBeginning == False:
		index = index - 1
		beforeString = savedOutputs[index] + beforeString
		if len(beforeString) > 5:
			print(savedOutputs[index])
			foundBeginning = True

	index = savedOutputs.index(string)
	foundEnd = False
	afterString = ""
	maxIndex = len(savedOutputs) - 1
	while (index <= maxIndex) and foundEnd == False:
		index = index + 1
		afterString = afterString + savedOutputs[index]
		if len(afterString) > 5:
			print(savedOutputs[index])
			foundEnd = True

	outputString = beforeString + "%p" + afterString
	return outputString

def reportInfoleak(region, string, leakOffset):
	global reportBugs
	if reportBugs == True:
		return

	infoleak = ["infoleak", [None, None, None, region, string, leakOffset, 0]]

	if outputFile != None:
		print("dumping")
		#if os.path.exists(outputFule):
		#	output = open(outputFile, "a")
		#else:
		output = open(outputFile, "w")
		pickle.dump(infoleak, output)
		output.close()	
	else:

		print("Breaking the pattern: %s" % str(infoleak))	

crashAnalysis = []
def gotCrash():
	print("Falls down")
	global outputFile
	global crashAnalysis
	global savedOutputs
	returnAddress = getReturnAddress()
	print("ffffFalls down")
	if (isMappedMemory(returnAddress) == False):
		reveresedReturnAddress = reverseInt(returnAddress)
		print("and ever")
		isFromInput, whichInput, offset = isValueFromInput(reveresedReturnAddress)
		if isFromInput != False:
			print("to hide")
			reportBufferOverflow(offset)

	print("i've come undone: %s" % str(crashAnalysis))
	for analysis in crashAnalysis:
		print("beneath")
		print(analysis)
		print("the")
		print(analysis[0])
		print("sun")
		if analysis[0] == "stackInfoleak":
			print("\n\nSaved Outputs: %s\n\n" % str(savedOutputs))

			stackLeak = analysis[1]

			leakOffsetFromStart = stackLeak[1]
			returnAddressAddress = getReturnAddressAddress()
			raaOffsetFromStart = returnAddressAddress - stack["start"]
			leakOffsetFromInput = (raaOffsetFromStart - offset) - leakOffsetFromStart

			infoleakOutput = stackLeak[2]

			string = getStringsBeforeAfter(infoleakOutput)
			reportInfoleak("stack", string, leakOffsetFromInput)

		elif analysis[0] == "infoleak":
			leak = analysis[1]

			region = leak[0]
			offset = leak[1]
			infoleakOutput = leak[2]


			string = getStringsBeforeAfter(infoleakOutput)

			reportInfoleak(region, string, offset)

		elif analysis[0] == "check_main32_offset":
			print("beneath the sun")
			if outputFile != None:
				print("dumping")
				output = open(outputFile, "w")
				pickle.dump(infoleak, output)
				output.close()
			else:
				print("Actual offset is: %s" % hex(offset))	

	sys.exit(0)

'''
def isAddressInCurrentStack():
	target.sendline("p $rbp")
	print("hello %s: " % rbp)
'''

def isStackAddress(address):
	if (address >= stack["start"]) and (address <= stack["end"]):
		return True
	return False


def stripContinuing(output):
	try:
		string = "Continuing.\n"
		stringLen = len(string)
		newIndex = output.find(string)
		#print("gravity: %s" % str(newIndex))
		return output[newIndex + stringLen:]
	except:
		return None

lastInput = None
savedOutputs = []
def processOutput(output):
	global lastInput
	global savedOutputs
	output = stripContinuing(output)
	if output == None:
		return

	outputLen = len(output)
	if outputLen == 0:
		return

	#strippedOutput = stripContinuing(output)
	#print(output)
	#print("The color of your fear: %s" % str(strippedOutput))
	if "SIGSEGV" in output:
		gotCrash()

	if "exited" in output:
		return

	if "0x" in output:
		#print("\n\n\nA life that's so demanding: %s\n\n\n" % str(output.strip("\n")))

		#print("\nI can't speak: %d\n"% len(output.strip("\n")))

		hasNumber = doesStringHaveNumbers(output)
		if hasNumber == False:
			savedOutputs.append(output)
			return

		queryMemoryRegions()
		value = parse0x(output)
		hexValue = hex(value)

		if isMappedMemory(value) == False:
			savedOutputs.append(output)
			return

		outputPieces = output.split(hexValue)



		infoleak = processInfoleak(value)
		print(infoleak)
		print(type(infoleak))

		infoleak.append(output)

		if isStackAddress(value) == True:
			crashAnalysis.append(["stackInfoleak", infoleak])

		else:
			crashAnalysis.append(["infoleak", infoleak])

		savedOutputs.append(output)
		return
		#reportInfoleak(infoleak)
		#print("hex value: %s" % hex(value))

		#print("libc: %s" % hex(libc["start"]))
		#print("pie: %s" % hex(pie["start"]))
		#print("stack: %s" % hex(stack["start"]))
			#print(output)


	savedOutputs.append(output)

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
def getInput():
	return target.recvuntil("gefffffffff")

def hi():
    try:
        x = getInput()
        #print("penguin\n\n\nOut is: %s\n\n\npenguin" % x)
        if "real as" in x:
        	#target.interactive()
        	#print("\n\n\n\n\nDENY THE SAVIOR\n\n\n\n")
        	gotCrash()
        	
        #raw_input()
        #print("Stage 1: %s" % x)
        x = x.split("\n\nThat's what")[0]
        #print("Stage 2: %s" % x)
        #x = x.split("Continuing.\n")[1]

        #print("Stage 3: %s" % x)
        if "SIGSEGV" in x:
        	gotCrash()
        return x
    except:
        return False




def setup():
	global target
	global targetBinary

	target = process(["gdb", ("%s" % targetBinary)])

	target.recvuntil("gefffffffff")

	target.sendline("catch syscall read write")

	#target.sendline("catch syscall write")

	target.recvuntil("gefffffffff")

	target.sendline("commands")

	target.sendline("silent")

	target.sendline("echo \\n\\nThat's what you do best\\n\\n")

	target.sendline("end")

	target.recvuntil("gefffffffff")

	target.sendline("catch signal SIGSEGV")

	target.recvuntil("gefffffffff")
	target.sendline("commands")

	target.sendline("silent")

	target.sendline("echo \\n\\nreal as ecer\\n\\n")

	target.sendline("end")

	target.recvuntil("gefffffffff")


	target.sendline("r")
	#

	x = target.recvuntil("gefffffffff").split("\n\nThat's what")

	target.sendline("c")
	target.recvuntil("Continuing.\n")


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

inputAnalysis = []
def sendInput():
	targetInput = genInput(2000)
	inputs.append(targetInput)
	target.sendline(targetInput)
	for analysis in inputAnalysis:
		print("Input Analysis Time")


def mainLoop():
	#
	#x = target.recvuntil("gef")
	#while "That's what" not in x:
	#	target.sendline("c")
	#	x = target.recvuntil("gef")
	i = 1
	x = hi()
	#x = target.recvuntil("gef").split("\n\nThat's what")[0].split("Continuing.\n")[1]
	exited = False
	#
	while exited == False:	
		print("1")
		while x != False:
			processOutput(x)

			if ("exited normally" in x) or ("not being run" in x):
				sys.exit(0)

			i += 1

			runCmd()
			target.sendline("c")
			x = hi()

		sendInput()

		x = z = hi()
		while x != False:
			x = hi()
		x = z

	print("yo")



bugFound = False
def mainCaller(recursionDepth):
	global bugFound
	#print("\n\nDepth is: %d\n\n" % recursionDepth)
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

def doesPointToZero(address):
	target.sendline("x/x %s" % hex(address))
	value = target.recvuntil("gefffffffff").split("\n")[0].split(":")[1]
	if parse0x(value) == 0:
		return True
	return False

def getPieRw():
	target.sendline("vmmap")
	memMappings = target.recvuntil("gefffffffff").split("\n")[2:-1]

	for line in memMappings:
		if ("rw" in line) and (targetBinary in line):
			print("line is: %s" % str(line))
			address = parse0x(line.split(" ")[0])

	while doesPointToZero(address) == False:
		address = address + 8

	if outputFile != None:
		output = open(outputFile, "w")
		pickle.dump(address, output)
		output.close()	

reportBugs = True
def runCmd():
	global reportBugs
	global crashAnalysis


	if command == "sanity_check":
		sys.exit(0)

	elif command == "get_pie_rw":
		getPieRw()
		sys.exit(0)

	elif command == "check_main32_offset":
		reportBugs = False
		crashAnalysis.append(["check_main32_offset"])

command = None

def setCommand(cmd):
	global command
	command = cmd

if __name__ == "__main__":
	global targetBinary
	global target
	parser = argparse.ArgumentParser(description = "Anaylzer for binaries using gdb")


	parser.add_argument("-b", metavar="-B", type=str, help="The Bianry to analyze", default = None)
	parser.add_argument("-o", metavar="-O", type=str, help="The output file", default = None)
	parser.add_argument("-c", metavar="-C", type=str, help="Give command to look for specific thing", default=None)

	args = parser.parse_args()

	targetBinary	= args.b
	outputFile 		= args.o
	command 		= args.c

	if targetBinary == None:
		helpFunction()

	if command != None:
		setCommand(command)

	#mainCaller(0)
	setup()
	mainLoop()
targetBinary = "hi"
outputFile = None
target = None