available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
print("We have: ")
print(available_toppings)
print("\n")

requested_toppings = []

prompt = ("What topping you want?")
prompt += ("(Enter 'quit' to finish) ")

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        requested_toppings.append(topping)
        for requested_topping in requested_toppings:
            if requested_topping in available_toppings:
                print('add ' + requested_topping + ' in pizza')
            else:
                print('we dont have ' + requested_topping)
                del requested_toppings[-1]
