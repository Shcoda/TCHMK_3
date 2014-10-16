#!/usr/bin/python
import bigClass
import sys

def printHelp():
	print "Usage: "
	print "TCHMK_1 <A filelame> <operation> <B filelame> <result filename> [-b] [<modulus filename>]"
	print "  -b for operations with binary files"


def process(A, B, md, op):
	zero = bigClass.bigClass("0")
	res = zero
	
	if (md < zero):
		print "Negative modulus!"
		return False, res
		
	if op == '+':
		res = A + B
		
	elif op == '-':
		res = A - B
		
	elif op == '*':
		res = A * B
		
	elif op == '/':
		res = A / B
		
	elif op == '%':
		res = A % B
		
	if (md > zero):
			res = res % md
			while (res < zero):
				res = res + md
				
	if op == '^':
		if md == zero:
			res = A ^ B;
		else:
			res = bigClass.powModClass(A, B, md)
				
	return True, res

	
def main():
	if len(sys.argv) < 5:
		print "Too few arguments passed."
		printHelp()
		return -1
		
	if len(sys.argv) > 7:
		print "Too many arguments passed."
		printHelp()
		return -1
		
	file1 = sys.argv[1]
	op = sys.argv[2]
	file2 = sys.argv[3]
	fileRes = sys.argv[4]
	bin = False
	fileMod = None
	
	if len(sys.argv) == 6:
		if sys.argv[5] == "-b":
			bin = True
		else:
			fileMod = sys.argv[5]
			
	if len(sys.argv) == 7:
		bin = True;
		fileMod = sys.argv[6]
		
	A = bigClass.bigClass("0")
	B = bigClass.bigClass("0")
	md = bigClass.bigClass("0")
	
	if bin == True:
		A.readBin(file1)
		B.readBin(file2)
		if fileMod != None:
			md.readBin(fileMod)
	else:
		A.readText(file1)
		B.readText(file2)
		if fileMod != None:
			md.readText(fileMod)

	isProcess, res = process(A, B, md, op)
	if not isProcess:
		sys.exit(-1)	
		
	if bin == True:
		res.writeBin(fileRes)
	else:
		res.writeText(fileRes)		

if __name__ == "__main__":
	main()