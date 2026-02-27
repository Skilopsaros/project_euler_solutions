from common import functions as cf

def main():
	right_truncatable_primes = {1:[2,3,5,7]}
	n_digits = 2
	doubly_truncatable_primes = []
	while len(doubly_truncatable_primes)<11:
		right_truncatable_primes[n_digits] = []
		for base_p in right_truncatable_primes[n_digits-1]:
			for added_p in [1,2,3,5,7,9]:
				number = base_p + pow(10,n_digits-1)*added_p
				if cf.is_prime(number):
					right_truncatable_primes[n_digits].append(number)
					if is_left_truncatable(number):
						doubly_truncatable_primes.append(number)
		n_digits += 1
	return(sum(doubly_truncatable_primes))

def is_left_truncatable(n):
	new_n = n
	while new_n > 0:
		if not cf.is_prime(new_n):
			return(False)
		new_n //= 10
	return(True)


if __name__ == "__main__":
	print(main())