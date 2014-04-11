import sys
import math


while True:
	numbers = str(input()).split();
	girls = int(numbers[0])
	boys = int(numbers[1])
	if girls == -1 and boys == -1:
		break
	elif girls == 0:
		print(boys)
	elif boys == 0:
		print(girls)
	else:
		maxGender = max(girls, boys)
		minGender = min(girls, boys)
		print(math.ceil(maxGender/(minGender + 1)))

