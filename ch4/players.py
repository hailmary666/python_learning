players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print('2-4')
print(players[1:4])
print('first-3')
print(players[:3])
print('3-last')
print(players[2:])
print('3-last')
print(players[-3:])
print('first three players:')
for player in players[:3]:
    print(player.title())
