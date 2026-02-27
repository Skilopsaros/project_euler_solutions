def main():
	constant = ""
	for i in range(1,1000000):
		constant += str(i)
	product = 1
	for i in range(7):
		print(int(constant[pow(10,i)-1]))
		product *= int(constant[pow(10,i)-1])
	return(product)

if __name__ == "__main__":
	print(main())
