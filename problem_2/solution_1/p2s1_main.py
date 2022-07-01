
def main(up_to):
	sum = 0
	fib_1 = 1
	fib_2 = 1
	new = 1


	while fib_1 < up_to:

		if 0 == (new % 2):
			sum += new

		new = fib_1 + fib_2
		fib_2 = fib_1
		fib_1 = new
	
	return(sum)


if __name__ == "__main__":
	print(main(4000000))