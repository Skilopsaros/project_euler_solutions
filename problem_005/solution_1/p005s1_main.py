import math as maths
from common import functions as cf

def main(up_to):
	primes = cf.find_primes(up_to+1)

	factorised_dict = {}
	for i in range(2, up_to+1):
		prime_factors = cf.find_prime_factors(i)
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



if __name__ == "__main__":
	print(main(20))