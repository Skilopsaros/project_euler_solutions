import math as maths

def main(input):
	return(maths.factorial(2*input)/pow(maths.factorial(input),2))

if __name__ == "__main__":
	print(main(20))