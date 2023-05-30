def check_tuple_lengths(*tuples):
    lengths = set(len(t) for t in tuples)
    return len(lengths) == 1

# Example usage:
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
tuple3 = (True, False)

print(check_tuple_lengths(tuple1, tuple2, tuple3))  # Output: True

tuple4 = (1, 2, 3, 4)
tuple5 = ('a', 'b')
tuple6 = (True, False, True)

print(check_tuple_lengths(tuple4, tuple5, tuple6))  # Output: False
