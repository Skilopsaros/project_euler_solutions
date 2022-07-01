
def main(up_to):
	i = 1
	sum = 0
	fib_1 = 1
	fib_2 = 1
	new = 1

	while fib_1 < up_to:
		i += 1
		if 3 == i:
			sum += new
			i =0

		new = fib_1 + fib_2
		fib_2 = fib_1
		fib_1 = new
	
	return(sum)


if __name__ == "__main__":
	print(main(4000000))