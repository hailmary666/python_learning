fav_otpusk = {}

opros = True

while opros:
    name = input("Please enter your name: ")
    mesto = input("Where do you like to chill? ")
    fav_otpusk[name] = mesto
    repeat = input("You want ask next person? (yes/no) ")
    if repeat == 'no':
        opros = False

print("\n---Results---")
for name,mesto in fav_otpusk.items():
    print(name + " like to visit " + mesto)
