def shopping_decorator(func):
    """
    Decorator for shopping function
    """
    def wrapper(type, *list, **groups):
        """
        Wrapper function to call the shopping function
        """
        print(type.upper() + '!')
        func(type, *list, **groups)
    return wrapper


@shopping_decorator
def shopping(type, *list, **groups):
    """
    Prints information about shopping
    """
    print("Let's do", type, "shopping!")
    print()
    print('Main list: ', end='')

    for i in list:
        print(i, end=' ')

    print()
    print()
    print('Groups:')

    keys = groups.keys()
    for key in keys:
        print('->', key, '---', groups[key])
        

# Call shopping function

shopping('food', 'bread', 'meat', 'rice', fruits=['apple', 'banana', 'pineapple'], drinks=['water', 'milk'])