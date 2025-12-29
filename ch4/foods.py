my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('ice cream')
friend_foods.append('cannoli')
friend_foods.append('pussy')
print('my fav foods:')
for food in my_foods:
    print(food)
print('\nmy friend`s favorite foods are:')
for ffood in friend_foods:
    print(ffood)
#z10
print('\nfirst three items in my foods are')
print(my_foods[:3])
print('three items from the middle in friend foods are')
print(friend_foods[1:4])
print('three last items in friend foods are')
print(friend_foods[-3:])
