
def main(digits):
	fibonachi = [1,1]
	while fibonachi[-1]<pow(10,digits-1):
		fibonachi.append(fibonachi[-1]+fibonachi[-2])
	return(len(fibonachi))

if __name__ == "__main__":
	print(main(1000))