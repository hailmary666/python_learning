favorite_places = {
        'voronezh': ['maria', 'bobby', 'john'],
        'moscow': ['maria', 'leo'],
        'samara': ['maks'],
        }

for place, names in favorite_places.items():
    for name in set(names):
        print(name.title() + "'s fav place is " + place.title() + "\n")
            
