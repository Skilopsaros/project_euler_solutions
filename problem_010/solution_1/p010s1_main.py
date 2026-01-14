import numpy as np
from common import functions as cf

def main(up_to):
	primes_list = cf.find_primes(up_to)
	return(np.sum(np.array(primes_list)))


if __name__ == "__main__":
	print(main(2000000))