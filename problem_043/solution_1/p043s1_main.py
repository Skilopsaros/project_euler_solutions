from common import functions as cf

def main():
	permutations = cf.find_all_permutations(list(range(10)))
	sum_perms_with_property = 0
	for permutation in permutations:
		if has_property(permutation):
			sum_perms_with_property += cf.permutation_to_number(permutation)
	return(sum_perms_with_property)
	


def has_property(permutation):
	primes = [2,3,5,7,11,13,17]
	for i in range(7):
		if int(permutation[i+1]*100+permutation[i+2]*10+permutation[i+3])%primes[i] != 0:
			return(False)
	return(True)


if __name__ == "__main__":
	# print(has_property(["1","4","0","6","3","5","7","2","8","9"]))
	print(main())
