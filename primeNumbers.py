# Find the if numbers 3 - 100 are prime numbers
# prime numbers are numbers 

def isPrime(num, i):
    if num <= 1:
        return False
    
    for possible_factor in range(2, num):
        if num % possible_factor == 0:
            return False
    
    return True

for num in range(3, 101):
    if isPrime(num,2):
        print(num , True)
    else:
        print (num , False)
        