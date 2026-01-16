def main(size):
	all_answers = set()
	for i in range(2, size+1):
		for j in range(2, size+1):
			all_answers.add(pow(i,j))
	return(len(all_answers))
		
if __name__ == "__main__":
	print(main(100))