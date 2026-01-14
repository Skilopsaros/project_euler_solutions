from common import functions as cf

def main(up_to):
    amicable = set()
    for i in range(up_to):
        if i not in amicable:
            amicable_i, pair = is_amicable(i)
            if amicable_i:
                amicable.add(i)
                if pair < up_to:
                    amicable.add(pair)
    return(sum(amicable))

def is_amicable(input_number):
    pair = cf.sum_of_proper_divisors(input_number)
    return((cf.sum_of_proper_divisors(pair) == input_number) and (input_number!=pair), pair)
    
    

if __name__ == "__main__":
    print(main(10000))