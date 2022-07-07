import math as maths
import copy

def main(n_divisors):
	i = 3
	n = 3
	while find_number_of_factors(n) <= n_divisors:
		print(n)
		n += i
		i += 1
	return(n)

def find_number_of_factors(input):
	primes = find_primes(input+1)
	prime_factors = find_prime_factors(input, primes)
	prime_appearances_dict = {}
	for prime in prime_factors:
		prime_appearances_dict[str(prime)] = prime_factors.count(prime)

	n_factors = 1
	for value in prime_appearances_dict.values():
		n_factors *= value+1
	

	return(n_factors)



def find_prime_factors(input, primes, start = 2, factors_list = None):
	if None == factors_list:
		factors_list = []
	check_number = input
	if input in primes:
		return([input])
	for i in range(start, int(input/2+1)):
		if i in primes:
			div, mod = divmod(check_number, i)
			if 0 == mod:
				factors_list.append(i)
				if div in primes:
					factors_list.append(div)
					return(factors_list)
				return(find_prime_factors(div, primes, i, factors_list))

def find_primes(up_to, primes_list = [2]):
	for i in range(max(primes_list)+1, maths.ceil(up_to)):
		if is_next_prime(i, primes_list):
			primes_list.append(i)
	return(primes_list)

def is_next_prime(n, list):
	for i in list:
		if (maths.floor(pow(n,0.5))+1) < i:
			return(True)
		if n%i==0:
			return(False)
	return(True)

if __name__ == "__main__":
	print(main(500))