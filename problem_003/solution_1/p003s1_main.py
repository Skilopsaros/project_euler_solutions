import math as maths
import common.functions as cf

def main(input_number, start = 2):
	return(max(cf.find_prime_factors(input_number)))

if __name__ == "__main__":
	print(main(600851475143))