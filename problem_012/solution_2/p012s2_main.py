import time
import copy
from common import functions as cf

def main(n_divisors):
	# the nth triangle number Tn = n(n+1)/2
	m_1 = 2
	dict_1 = cf.find_prime_factors(m_1, as_dict=True)
	m_2 = 3
	dict_2 = cf.find_prime_factors(m_2, as_dict=True)
	while True:
		check = get_number_of_factors(combine_prime_dicts(dict_1, dict_2))
		if check > n_divisors:
			return(m_1*m_2)
		m_2 += 2
		dict_2 = cf.find_prime_factors(m_2, as_dict=True)

		check = get_number_of_factors(combine_prime_dicts(dict_1, dict_2))
		if check > n_divisors:
			return(m_1*m_2)
		m_1 += 1
		dict_1 = cf.find_prime_factors(m_1, as_dict=True)

def combine_prime_dicts(dict_1, dict_2):
	end_dict = copy.copy(dict_1)
	for key in dict_2.keys():
		if key in end_dict:
			end_dict[key] = dict_1[key] + dict_2[key]
		else:
			end_dict[key] = dict_2[key]
	return(end_dict)

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
