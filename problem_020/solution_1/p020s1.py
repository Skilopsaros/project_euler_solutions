import math as maths

def main(input):
	sum = 0
	num = str(maths.factorial(input))
	for n in num:
		sum += int(n)
	return(sum)

if __name__ == "__main__":
	print(main(100))