def palindromes(expression):
    """
    Returns True if expression is palindrome and False otherwise.
    """
  
    expression = expression.replace(' ', '')
    expression = expression.lower()
  
    if expression[:] == expression[::-1]:
        return True

    return False

