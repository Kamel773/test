def split_list_of_lists(lst):
    first_elements = [sublist[0] for sublist in lst]
    second_elements = [sublist[1] for sublist in lst]
    return [first_elements, second_elements]
