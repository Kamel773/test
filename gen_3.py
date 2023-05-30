def count_occurrences(string):
    count = 0
    index = 0
    while index < len(string):
        index = string.find('std', index)
        if index == -1:
            break
        count += 1
        index += 3  # Move the index after the found occurrence
    return count
