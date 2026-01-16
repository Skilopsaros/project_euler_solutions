from common import functions as cf

def main(up_to):
	primes = cf.find_primes(up_to)
	result_n = 0
	result_a = 0
	result_b = 0
	for b in primes:
		for a in range(-b,1000):
			n = primes_from_formula(a,b)
			if n > result_n:
				result_n, result_a, result_b = n, a, b
	print(f"n {result_n}, a {result_a}, b {result_b}")
	return(result_a*result_b)

def primes_from_formula(a,b):
	i = 0
	new_value = b
	while (new_value > 0) and cf.is_prime(new_value):
		i+=1
		new_value = i*i+a*i+b
	return(i)

if __name__ == "__main__":
	print(main(1000))