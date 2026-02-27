from common import functions as cf

def main():
	prime_pandigitals = []
	for i in range(8):
		found = False
		permutations = cf.find_all_permutations(list(range(1,10-i)))
		for permutation in permutations:
			pandigital = cf.permutation_to_number(permutation)
			if cf.is_prime(pandigital):
				prime_pandigitals.append(pandigital)
				found = True
		if found:
			break
	return(max(prime_pandigitals))
			

if __name__ == "__main__":
	print(main())
