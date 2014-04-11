import sys

tests = int(input())
while tests > 0:
	numbers = str(input()).split()
	a = int(numbers[0])
	b = int(numbers[1])
	exp = pow(a, b, 10)
	c = a**exp
	lastDig = str(c)[-1]
	print(lastDig)
	tests -= 1
	
	
