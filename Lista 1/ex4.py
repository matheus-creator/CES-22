def is_prime(n):
    """
    Returns True if n is prime and False otherwise.
    """
  
    for i in range(2, n):
        if n % i == 0:
            return False
  
    return True

