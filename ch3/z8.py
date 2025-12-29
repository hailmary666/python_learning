country = ['paris', 'berlin', 'lisabon', 'new_york', 'tokyo']
#Original_list
print('original_list')
print(country)
#Sorted_list
print('sorted list')
print(sorted(country, reverse = True))
#Original_again
print('original again')
print(country)
#Reverse
country.reverse()
print('reversed list')
print(country)
#Unreverse
country.reverse()
print('unreversed list')
print(country)
#Const_sorted
country.sort()
print('const sorted')
print(country)
#Const_sorted_z-a
country.sort(reverse=True)
print('const sorted but reverse')
print(country)
