import numpy as np

def main(up_to):
	numbers_array = np.arange(1,up_to+1)
	return(pow(np.sum(numbers_array),2) - np.sum(pow(numbers_array,2)))

if __name__ == "__main__":
	print(main(100))