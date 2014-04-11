import sys

tests = int(input())
while (tests > 0):
	numbers = str(input()).split()
	num1 = numbers[0]
	num2 = numbers[1]
	num1rev = num1[::-1]
	num2rev = num2[::-1]
	result = int(num1rev) + int(num2rev)
	result = str(result)[::-1]

	resInt = int(result)
	print(str(resInt))

	tests -= 1