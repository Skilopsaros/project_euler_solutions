

def all_permutations(digits):
	permutations = []
	for digit in digits:
		list_without_digit = [d for d in digits if d != digit]
		if len(list_without_digit) == 2:
			remaining_permutations = permutations_of_two_digits(list_without_digit)
		else:
			remaining_permutations = all_permutations(list_without_digit)
		permutations.extend([[digit]+p for p in remaining_permutations])
	return(permutations)

def permutations_of_two_digits(digits):
	return([[digits[0],digits[1]],[digits[1],digits[0]]])

def main(digits, element):
	permutation_lists = all_permutations(digits)
	permutations = []
	for permutation_list in permutation_lists:
		permutations.append("".join(str(d) for d in permutation_list))
	permutations.sort()
	return(permutations[element-1])

if __name__ == "__main__":
	print(main([0,1,2,3,4,5,6,7,8,9], 1000000))