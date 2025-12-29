numbers = {'maria': [1, 5, 10],
           'bob': [1],
           'andrew': [7, 21, 98],
           'elize': [5, 33, 555],
           'walt': [10, 666, 2],
           }

for name, numbers in numbers.items():
    if len(numbers) > 1:
        print(name.title() + "'s fav numbers are:")
    else:
        print(name.title() + "'s fav number is:")
    for number in numbers:
        print("\t" + str(number))
