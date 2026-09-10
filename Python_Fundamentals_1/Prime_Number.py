


def allPrimesUpTo(num):
##  start with prime 2 being known 
    all_primes = [2]
    primes = True
    Square_root_prime = num ** 0.5
    if Square_root_prime % 1 == 0: 
            return print("The number is a perfect square and not prime") 
### need a while loop because I will continuously add to my list with the current program 
    while primes == True: 
           
#I want to iterate through my list, it may be empty or not and stop at 
        for number in range(2, int(Square_root_prime) + 1):
            print(number)
            # ## if the number is divisible by any of the primes in the list, then it is not prime
            ### I want to see if the number is divisible by any of the primes in the list, if it is then it is not prime and I will return a message saying so
            for prime in all_primes:
                if number % prime == 0:
                    break 
                elif
            # if num % all_primes[number] == 0:
            #     return print(f'The number {num} is not prime because it is divisible by {all_primes[number]}')
            # elif num % all_primes[number] != 0:
            #     while primes == True: 
   
            #         print(f'adding to the list')
            #         all_primes = all_primes + [num]
            #         break  
            

allPrimesUpTo(27)



