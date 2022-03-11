def sum_to(n):
    """
    Returns the sum of all integer numbers up to and including n.
    """
  
    sum = 0
    for i in range(n):
        sum += i + 1
  
    return sum

print(sum_to(10))