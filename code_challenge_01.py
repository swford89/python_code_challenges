# Coding Nomads - Code Challenge #1: The Sieve of Eratosthenes
# Scott Ford

def sieve(n):
    sieve_list = [] 

    if n in range(2,65536):                                 # make sure min and max values are >= 2 and < 65,536
        for p in range(2,n):                                # get numbers in the specified range
            sieve_list.append(p)                            # append those numbers to the sieve list
    else:
        print("Eratosthenes doesn't like this number.")
        
    for num in range(2,n):                                  # get potential multiples of numbers in the range of your list
        for p in sieve_list:                                # get your p values
            if num * p in sieve_list:                       # check if multiple * p is in the list
                sieve_list.remove(num * p)                  # remove the resultant multiple 
    

    print(*sieve_list, sep=", ", end="" + "\n")        

num_limit = int(input("Eratosthenes would like the number up to which you're looking for primes: "))

sieve(num_limit)
