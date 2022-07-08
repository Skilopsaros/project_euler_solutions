def main(input):
	num = pow(2,input)
	return(sum_digits(num))

def sum_digits(input):
	sum = 0
	for i in str(input):
		sum += int(i)
	return(sum)

if __name__ == "__main__":
	print(main(1000))