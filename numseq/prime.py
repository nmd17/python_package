def primes(n):
    temp = []
    for i in range(n):
        if is_prime(i):
            temp.append(i)

    return temp
            
def is_prime(m):
    # Corner cases 
    if (m <= 1) : 
        return False
    if (m <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (m % 2 == 0 or m % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= m) : 
        if (m % i == 0 or m % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True