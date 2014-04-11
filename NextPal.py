import sys		

cases = int(input())
while(cases > 0):
	number = int(input())
	number += 1
	while(True):
		if(str(number)[0] == str(number)[-1]):
			if(str(number) == str(number)[::-1]):
				print(number)
				break
			else:
				number += 1
		else:
			number += 1
		
	cases -= 1
		