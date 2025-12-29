#Original dic
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}

for alien in aliens[:5]:
    print(alien)
print("...")

#Add new keys with values
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

print("Original x-position: " + str(alien_0['x_position']))

#Alien move to right
#Calulating value of movement on 'speed'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#New position = old position + incriesed
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']) + ".")

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + (alien_0['color']) + ".")

del alien_0['points']
print(alien_0)
