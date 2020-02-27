from pwn import *

from functools import wraps
import errno
import os
import signal
import time

hexChars = [0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39]
def parse0xInfoleak(string):
	startIndex = string.find("0x")

	stringLen = len(string)
	index = startIndex + 2
	foundEnd = False
	while foundEnd == False:

		if string[index] not in hexChars:
			print(string[index])
			index = index + 1
			if index >= (stringLen - 1):
				foundEnd = True


	hexString = string[startIndex:index]
	hexValue = int(hexString, 16)

	preceedingString = string[:startIndex]
	proceedingString = string[index]
	return [preceedingString, proceedingString, hexValue]


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
	memMappings = target.recvuntil("gef").split("\n")[1:-1]
	print("live as")
	for line in memMappings:
		lineParts = line.split(" ")
		#print("lineparts is: %s" % str(lineParts))
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
	
def processOutput(output):
	outputLen = len(output)
	if outputLen == 0:
		return

	hasNumber = doesStringHaveNumbers(output)
	if hasNumber == False:
		return

	if "0x" in output:
		parsedInfoleak = parse0xInfoleak(output)
		print("output is: %s" % str(parsedInfoleak))
		print("Infoleak is: %s" % hex(parsedInfoleak[2]))
		queryMemoryRegions()
		infoleak = processInfoleak(parsedInfoleak[2])
		if infoleak != None:
			reportInfoleak(infoleak)
		#print("Infoleak is: %s" % str(infoleak))

		target.interactive()
		sys.exit()


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

targetBinary = "hi"

target = process(["gdb", ("./%s" % targetBinary)])

target.recvuntil("gef")

target.sendline("catch syscall read")

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

x = target.recvuntil("gef").split("\n\nThat's what")[0].split("Continuing.\n")[1]

exited = False

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


