users = []

if users:
    for user in users:
        if user == 'admin':
            print('hello boossssss')
        else:
            print('hello ' + user.title())
else:
    print('we need users')
