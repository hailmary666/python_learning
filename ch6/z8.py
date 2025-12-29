bobby = {
        'name': 'bobby',
        'vid': 'cat',
        'owner': 'maria',
        }
groovy = {
        'name': 'groovy',
        'vid': 'dog',
        'owner': 'gary',
        }
stupid = {
        'name': 'stupid',
        'vid': 'pig',
        'owner': 'john',
        }
pets = [bobby, groovy, stupid]

for pet in pets:
    print("Pet name: " + pet['name'].title())
    print("\nVid: " + pet['vid'])
    print("\nOwner name: " + pet['owner'].title())
    print("________________________________________________\n")
