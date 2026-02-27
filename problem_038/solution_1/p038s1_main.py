from common import functions as cf

def main():
	good_pandigitals = []
	permutations = cf.find_all_permutations([1,2,3,4,5,6,7,8,9])
	for permutation in permutations:
		pandigital = 0
		for i,v in enumerate(permutation):
			pandigital += v*pow(10,i)
		if is_concat_formable(pandigital):
			good_pandigitals.append(pandigital)
	return(max(good_pandigitals))
		

def is_concat_formable(n):
	for n_digits in range(1,5):
		separated_numbers = [str(n)[:n_digits]]
		while True:
			new_number = str(int(separated_numbers[0]) + int(separated_numbers[-1]))
			new_total = "".join(separated_numbers) + new_number
			if new_total != str(n)[:len(new_total)]:
				break
			separated_numbers.append(new_number)
		if len("".join(separated_numbers)) == len(str(n)):
			return(True)
	return(False)


if __name__ == "__main__":
	print(main())