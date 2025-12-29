favorite_languages = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'],
        'phil': ['python', 'haskell'],
        }

persons = ['jen', 'sarah', 'dominik', 'bob', 'ilya']

for person in persons:
    if person not in favorite_languages.keys():
        print("\n" + person.title() + " pls take our poll!")
    else:
        print("\n" + person.title() + " thanks")

print("_______________________________________________________")

friends = ['phil', 'jen']

for name, languages in favorite_languages.items():
    if len(favorite_languages[name]) == 1:
        for language in languages:
            print("\n" + name.title() + "'s fav lenguage is " + language.title())
    else:
        print("\n" + name.title() + "'s fav languages are:")
        for language in languages:
            print("\t" + language.title())
print("_______________________________________________________")

for name in sorted(favorite_languages.keys()):
    if name in friends:
        print("\nHello " + name.title() +
              ", i see your favorite language is ")
        for language in favorite_languages[name]:
            print(language)
    else:
        print("\n" + name.title())
print("_______________________________________________________")
#set()-vivod vseh zna4enii bez povtoreny
for name in set(favorite_languages.keys()):
    print("\n" + name.title())
print("_______________________________________________________")
