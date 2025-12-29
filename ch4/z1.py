pizzas = ['pepperoni', 'chiken', 'spicy']
print('i really love pizza')
friend_pizzas = pizzas[:]
pizzas.append('grill')
friend_pizzas.append('pussy')
print('my fav pizzas are')
for pizza in pizzas:
    print(pizza)
print('my friend`s fav pizzas are')
for fpizza in friend_pizzas:
    print(fpizza)
