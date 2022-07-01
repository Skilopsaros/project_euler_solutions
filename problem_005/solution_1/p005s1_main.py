import math as maths

def main(up_to):
	primes = find_primes(up_to+1)

	factorised_dict = {}
	for i in range(2, up_to+1):
		prime_factors = find_prime_factors(i, primes)
		prime_appearances_dict = {}
		for prime in primes:
			prime_appearances_dict[str(prime)] = prime_factors.count(prime)
		factorised_dict[str(i)] = prime_appearances_dict
	
	answer_factors_dict = {str(prime):0 for prime in primes}
	for factorised_number in factorised_dict.values():
		for key, value in factorised_number.items():
			if value > answer_factors_dict[key]:
				answer_factors_dict[key] = value
	
	answer = 1
	for key, value in answer_factors_dict.items():
		answer *= pow(int(key), int(value))
	return(answer)

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

def find_primes(up_to):
	primes_list = []
	for i in range(2, maths.ceil(up_to)):
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
	print(main(20))