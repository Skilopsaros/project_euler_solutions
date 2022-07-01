
def main(up_to):
	check_3 = 0
	check_5 = 0
	is_multiple = False
	sum = 0

	for i in range(up_to):
		if 3 == check_3:
			check_3 = 0
			is_multiple = True
		if 5 == check_5:
			check_5 = 0
			is_multiple = True
		if is_multiple:
			sum += i
			is_multiple = False
		check_3 += 1
		check_5 += 1
	
	return(sum)


if __name__ == "__main__":
	print(main(1000))