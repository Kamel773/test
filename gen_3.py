def count_identical_items(list1, list2, list3):
    count = 0
    min_length = min(len(list1), len(list2), len(list3))
    
    for i in range(min_length):
        if list1[i] == list2[i] == list3[i]:
            count += 1
    
    return count
