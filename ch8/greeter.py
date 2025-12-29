def get_formatted_name(first_name, last_name):

    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease enter your name:")
    print("(Press 'enter' to leave)")
    f_name = input("First name: ")
    if f_name == '':
        break
    l_name = input("Last name: ")
    if l_name == '':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name)

