import math as maths
import copy
import time

def remember_output(f):
	cache = {}
	def decorated_function(*args):
		if args not in cache:
			cache[args] = f(*args)
		return(cache[args])
	return(decorated_function)
	
@remember_output
def is_prime(n):
	if n in [0,1]:
		return False
	if n%2 == 0:
		return(n == 2)
	for i in range(3,maths.floor(pow(n,0.5))+1,2):
		if n%i==0:
			return(False)
	return(True)

def remember_primes(find_primes_function):
	primes_list = []
	largest_number_checked = 0
	def decorated_function(up_to):
		nonlocal largest_number_checked
		nonlocal primes_list
		if up_to <= largest_number_checked:
			small_primes_list = []
			for prime in primes_list:
				if prime < up_to:
					small_primes_list.append(prime)
			return(small_primes_list)
		largest_number_checked = up_to
		primes_list = find_primes_function(up_to, primes_list)
		return(primes_list)
	return(decorated_function)

@remember_primes
def find_primes(up_to, primes_list=[2]):
	if not primes_list:
		primes_list = [2]
	new_primes_list = copy.copy(primes_list)
	for i in range(max(primes_list), maths.ceil(up_to)):
		if is_next_prime(i, new_primes_list):
			new_primes_list.append(i)
	return(new_primes_list)

def is_next_prime(n, primes_list):
	sqrt = maths.floor(pow(n,0.5))+1
	for i in primes_list:
		if sqrt < i:
			return(True)
		if n%i==0:
			return(False)
	return(True)

def find_prime_factors(input_number, start = 2, factors_list = None, as_dict = False):
	if input_number == 1:
		if as_dict:
			return({})
		return([])
	if (not factors_list) and is_prime(input_number):
		if as_dict:
			return({input_number:1})
		return([input_number])
	new_factors_list = [] if None == factors_list else copy.copy(factors_list)
	check_number = input_number
	for i in range(start, int(input_number/2+1)):
		if is_prime(i):
			div, mod = divmod(check_number, i)
			if 0 == mod:
				new_factors_list.append(i)
				if is_prime(div):
					new_factors_list.append(div)
					if as_dict:
						return(prime_factors_list_to_dict(new_factors_list))
					return(new_factors_list)
				return(find_prime_factors(div, i, new_factors_list, as_dict=as_dict))

def prime_factors_list_to_dict(prime_factors_list):
	prime_factors_dict = {}
	for prime in prime_factors_list:
		prime_factors_dict[prime] = prime_factors_list.count(prime)
	return(prime_factors_dict)

def find_divisors(input_number, include_self = False):
	if input_number == 0:
		return(set())
	elif input_number == 1:
		return({1})
	prime_factors = find_prime_factors(input_number)
	factors = set()
	for i in range(pow(2, len(prime_factors))):
		bin_str = str(bin(i))[2:].zfill(len(prime_factors))
		if include_self or "0" in bin_str:
			factor = 1
			for j, d in enumerate(bin_str):
				if int(d):
					factor *= prime_factors[j]
			factors.add(factor)
	return(factors)

@remember_output
def sum_of_proper_divisors(input_number):
	return(sum(find_divisors(input_number)))

@remember_output
def fibonacci(n):
	if n in [1,2]:
		return(1)
	return(fibonacci(n-1)+fibonacci(n-2))


def simplify_fraction(n, d):
	n_factors = find_prime_factors(n, as_dict=True)
	d_factors = find_prime_factors(d, as_dict=True)
	for k, v in n_factors.items():
		if k in d_factors:
			min_multiplicity = min(v, d_factors[k])
			n_factors[k] -= min_multiplicity
			d_factors[k] -= min_multiplicity
	new_n = maths.prod([pow(k,v) for k,v in n_factors.items()])
	new_d = maths.prod([pow(k,v) for k,v in d_factors.items()])
	return(new_n, new_d)

def find_all_permutations(digits):
	if len(digits) == 1:
		return([digits])
	permutations = []
	for d in digits:
		new_digits = list(digits)
		new_digits.remove(d)
		new_permutations = find_all_permutations(new_digits)
		for permutation in new_permutations:
			permutation.append(d)
			permutations.append(permutation)
	return(permutations)

def permutation_to_number(permutation):
	pandigital = 0
	for i,v in enumerate(permutation[::-1]):
		pandigital += v*pow(10,i)
	return(pandigital)

def is_perfect_square(n):
	guess = int(pow(n,0.5))
	if guess*guess == n:
		return(True)
	if guess*guess < n:
		while guess*guess < n:
			guess += 1
		return(guess*guess==n)
	if guess*guess > n:
		while guess*guess > n:
			guess -= 1
		return(guess*guess==n)

def is_palindrome(a, b):
	return("".join(sorted(str(a)))=="".join(sorted(str(b))))

if __name__ == "__main__":
	print("new")
	start = time.time()
	# time here
	stop = time.time()
	print(stop-start)
	



	