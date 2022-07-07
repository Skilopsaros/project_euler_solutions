import math as maths
import copy

def main(n_divisors):
	i = 3
	n = 3
	while find_number_of_factors(n) <= n_divisors:
		n += i
		i += 1
	return(n)

def find_number_of_factors(input):
	primes = find_primes(input+1)
	prime_factors = find_prime_factors(input, primes)
	# factors = [1]
	prime_appearances_dict = {}
	for prime in prime_factors:
		prime_appearances_dict[str(prime)] = prime_factors.count(prime)

	all_factors_dicts = get_all_factor_dicts(prime_appearances_dict, list(prime_appearances_dict.keys()))

	# for factor_dict in all_factors_dicts:
	# 	factors.append(dict_to_number(factor_dict))
	# return(factors)

	return(len(all_factors_dicts)+1)

# def dict_to_number(prime_dict):
# 	number = 1
# 	for key, value in prime_dict.items():
# 		number *= pow(int(key), int(value))
# 	return(number)

def get_all_factor_dicts(dict, keys_to_do):
	subsets = construct_subsets(dict, keys_to_do)
	_ = subsets.pop(0)
	return(subsets)

def construct_subsets(dict, keys_to_do):
	key = keys_to_do.pop(0)
	sub_dicts = []
	all_sub_dicts = []
	for i in range(dict[key]+1):
		new_dict = copy.copy(dict)
		new_dict[key] = i
		sub_dicts.append(new_dict)
	if keys_to_do == []:
		return(sub_dicts)
	for sub_dict in sub_dicts:
		all_sub_dicts.extend(construct_subsets(sub_dict, copy.copy(keys_to_do)))
	return(all_sub_dicts)

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