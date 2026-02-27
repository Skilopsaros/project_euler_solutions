import copy
import math as maths


def main():
	curious_numbers = []
	for i in range(3, 2540160):# 7 digit number equal to 7*9!. any number larger than that is necessarily larger than the sum of the factorials of its digits
		if sum([maths.factorial(int(d)) for d in str(i)]) == i:
			curious_numbers.append(i)
	return(sum(curious_numbers))

if __name__ == "__main__":
	print(main())