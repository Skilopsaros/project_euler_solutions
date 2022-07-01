import math as maths

def main(sum_of_numbers):
	for i in range(1, sum_of_numbers//3):
		for j in range(i, sum_of_numbers//2):
			k = sum_of_numbers - i - j
			if pow(i,2) + pow(j,2) == pow(k,2):
				print(i, j, k)
				return(i*j*k)
	return("ERROR")

if __name__ == "__main__":
	print(main(1000))