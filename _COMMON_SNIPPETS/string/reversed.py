#%%
# Reversed for string
seq_string = 'Python'
print(list(reversed(seq_string)))       # ['n', 'o', 'h', 't', 'y', 'P']

# Reversed for tuple
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')      # ['n', 'o', 'h', 't', 'y', 'P']
print(list(reversed(seq_tuple)))

# Reversed for range
seq_range = range(5, 9)
print(list(reversed(seq_range)))            # [8, 7, 6, 5]

# Reversed for list
seq_list = [1, 2, 4, 3, 5]
print(list(reversed(seq_list)))             # [5, 3, 4, 2, 1]


# https://betterprogramming.pub/9-handy-python-functions-for-programmers-cc391a59acc7

# Sort & Reverse
my_list = ['D','C','B','A']
a = my_list.sort()

print(sorted(my_list, reverse=True))
