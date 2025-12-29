food = 'pizza'
print('pizza?')
print(food == 'pizza')
print('ass?')
print(food == 'ass')

name = 'Andrew'
print('Andrew?')
print(name.lower() == 'andrew')
print('Marie?')
print(name.lower() == 'marie')

number = 10
print('11 != 10?')
print(number != 11)
print('10 = 10?')
print(number == 10)
print('14 > 10?')
print(number < 14)

number = 10
print('14, 15 > 10?')
print(number < 14 or 15)
print('9, 7 < 10?')
print(9 and 7 < number)

cars = ['audi', 'bmw']
print(cars)
print('audi in cars?')
car = 'audi'
print(car in cars)
print('shit not in cars?')
car = 'shit'
print(car not in cars)
