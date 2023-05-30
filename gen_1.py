def flatten_and_sum(lst):
    flattened_list = []
    for item in lst:
        if isinstance(item, list):
            flattened_list.extend(flatten_and_sum(item))
        else:
            flattened_list.append(item)
    return sum(flattened_list)
