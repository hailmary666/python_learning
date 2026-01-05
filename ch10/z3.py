filename = 'guest.txt'

prompt = "Enter your name:"
prompt += "\n(enter 'q' to quit) "
while True:
    name = input(prompt)
    if name != 'q':
        answer = "Hello, " + name.title() + "\n"
        print(answer)

        with open(filename, 'a') as file_object:
            file_object.write(answer)
    else:
        break
