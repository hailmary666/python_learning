persons = ['Bob', 'Garry', 'Elena', 'Arian']
print(persons)
#Lenth list
print('lenth of list is')
print(len(persons))
#Print first name
print('first in list is: ' + persons[0])
#Add person in end of list
persons.append('Ivan')
print('new list with added person in end')
print(persons)
#Add person in choosen slot
persons.insert(1, 'Maria')
print('person in slot 2 added')
print(persons)
#Delete person in choosen slot but remembered
removed = persons.pop(1)
print('removed person')
print(removed)
print('new list')
print(persons)
#Delete person forever
del persons[0]
print('first person was deleted')
print('new list')
print(persons)
#Change person
persons[0] = 'Jack'
print('first person was changed')
print(persons)
#Remove person by name
removed = 'Jack'
persons.remove(removed)
print(removed + ' was removed')
#Sorted by abc reversed
print('sorted but reversed list')
print(sorted(persons, reverse = True))
print('original list')
print(persons)
#Reversed
persons.reverse()
print('reversed list')
print(persons)
#Unreversed
persons.reverse()
print('unreversed list')
print(persons)
#Sorted forever
persons.sort()
print('sorted list')
print(persons)
