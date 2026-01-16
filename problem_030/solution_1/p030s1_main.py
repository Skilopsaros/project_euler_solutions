def main(power):
	numbers = []
	for i in range(2, power * pow(10, power)):
		if sum([pow(int(d),power) for d in str(i)]) == i:
			numbers.append(i)
	return(sum(numbers))
		
if __name__ == "__main__":
	print(main(5))