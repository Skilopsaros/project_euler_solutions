import math as maths
import numpy as np
import time

def main(size):
	square = np.array([[0 for i in range(size)] for j in range(size)])
	position = np.array([maths.floor(size/2) for i in range(2)])
	current_step = 0
	n_steps = 1
	current_direction = 0
	direction_repeaed = False
	directions = np.array([[1, 0],[0, -1],[-1, 0],[0, 1]])
	for i in range(1, size*size+1):
		square[position[0]][position[1]] = i
		position += directions[current_direction%4]
		current_step += 1
		if current_step >= n_steps:
			if direction_repeaed:
				n_steps += 1
				direction_repeaed = False
			else: 
				direction_repeaed = True
			current_direction += 1
			current_step = 0
	return(sum([square[i,i] for i in range(size)])+sum([square[size-i-1,i] for i in range(size)])-1)
		



if __name__ == "__main__":
	start = time.time()
	print(main(1001))
	stop = time.time()
	print(stop-start)