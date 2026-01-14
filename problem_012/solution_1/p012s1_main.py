import time
from common import functions as cf

def main(n_divisors):
	triangle_number = 3
	to_add = 3
	while True:
		prime_factors = cf.find_prime_factors(triangle_number, as_dict=True)
		number_of_prime_factors = get_number_of_factors(prime_factors)
		if number_of_prime_factors > n_divisors:
			return(triangle_number)
		triangle_number += to_add
		to_add += 1


def get_number_of_factors(prime_appearances_dict):
	n_factors = 1
	for value in prime_appearances_dict.values():
		n_factors *= value+1
	
	return(n_factors)

if __name__ == "__main__":
	start = time.time()
	print(main(500))
	stop = time.time()
	print(stop-start)
