reki = {
        'nil': 'egypt',
        'lena': 'russia',
        'govnorechka': 'ukraine',
        }
for vivod in reki:
    print("The " + vivod.title() +
          " runs through " + reki[vivod].title())

print("___________________________________________________")

print("\nCountrys:")
for vivod in reki.values():
    print(vivod.title())

print("\nRivers:")
for vivod in reki.keys():
    print(vivod.title())
