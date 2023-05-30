def newman_conway(n):
    # Base cases
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    # Recursive case
    return newman_conway(newman_conway(n - 1)) + newman_conway(n - newman_conway(n - 1))

# Testing the function
print(newman_conway(1))  # Output: 1
print(newman_conway(5))  # Output: 3
print(newman_conway(10)) # Output: 6
