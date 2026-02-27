from common import functions as cf

def main():
	s=0
	for i in range(1,1001):
		s+=pow(i,i)
	return(s)

if __name__ == "__main__":
	print(main())
