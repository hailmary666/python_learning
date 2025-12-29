cities = {
        'moscow': {
            'country': 'russia',
            'population': 5123225,
            'fact': 'great city',
            },
        'voronezh': {
            'country': 'russia',
            'population': 332342,
            'fact': 'bad city',
            },
        'paris': {
            'country': 'france',
            'population': 2281448,
            'fact': 'gay city',
            },
        }
for city, informations in cities.items():
    print(city.title() + ":")
    for information, value in informations.items():
        if information == 'country':
            print(information.title() + ": " +
                  value.title())
        else:
            print(information.title() + ": " +
                  str(value))
    print("_____________________________________________________________\n")
