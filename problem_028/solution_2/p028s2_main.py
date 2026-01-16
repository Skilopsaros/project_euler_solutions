import time

def main(size):
	current_number = 1
	running_sum = 1
	number_to_add = 2
	while current_number < size*size:
		running_sum += current_number*4 + number_to_add*10
		current_number += number_to_add*4
		number_to_add += 2
	return(running_sum)

if __name__ == "__main__":
	start = time.time()
	print(main(1001))
	stop = time.time()
	print(stop-start)