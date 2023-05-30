def is_undulating_number(number):
    # Convert the number to a string for easier manipulation
    number_str = str(number)
    
    # Iterate through the digits of the number
    for i in range(len(number_str)):
        # Check if the current digit is odd
        if int(number_str[i]) % 2 == 1:
            # Check if the next digit is even
            if i + 1 < len(number_str) and int(number_str[i + 1]) % 2 == 0:
                continue
            else:
                return False
        # Check if the current digit is even
        elif int(number_str[i]) % 2 == 0:
            # Check if the next digit is odd
            if i + 1 < len(number_str) and int(number_str[i + 1]) % 2 == 1:
                continue
            else:
                return False
    
    return True
