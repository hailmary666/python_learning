person_1 = {'first_name': 'leo',
          'last_name': 'kolmakov',
          'age': 21,
          'city': 'moscow',
          }
person_2 = {
        'first_name': 'ilya',
        'last_name': 'koznov',
        'age': 22,
        'city': 'voronezh',
        }
person_3 = {
        'first_name': 'maria',
        'last_name': 'jopova',
        'age': 14,
        'city': 'saratov',
        }
people = [person_1, person_2, person_3]

for person in people:
    full_name = person['first_name'].title() + " " + person['last_name'].title()
    age = person['age']
    city = person['city'].title()
    print("\nFull name: " + full_name)
    print("Age: " + str(age))
    print("Live in " + city)

