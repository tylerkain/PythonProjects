numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Tyler"
letters_list = [letter for letter in name]
print(letters_list)

range_of_numbers = range(1, 5)
new_list = [n * 2 for n in range_of_numbers]
print(new_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Freddie']

short_names = [name.upper() for name in names if len(name) >= 5]
print(short_names)
