import copy
import math as maths
from common import functions as cf


def main():
	curious_fractions = []
	for numerator  in range(10,100):
		for denominator in range(numerator +1,100):
			if (numerator %10 == 0) or (denominator%10 == 0):
				continue
			inds = []
			for k in range(2):
				anti_k = int(not k)
				if str(numerator )[k] == str(denominator)[anti_k]:
					inds.append((int(str(numerator )[anti_k]), int(str(denominator)[k])))
			for ind in inds:
				if cf.simplify_fraction(numerator ,denominator) == cf.simplify_fraction(*ind):
					curious_fractions.append(ind)
	result_numerator = 1
	result_denominator = 1
	for n,d in curious_fractions:
		result_numerator *= n
		result_denominator *= d
	return(cf.simplify_fraction(result_numerator, result_denominator))

if __name__ == "__main__":
	print(main())