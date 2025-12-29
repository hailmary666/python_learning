curret_users = ['alice', 'bob', 'nigga228', 'john', 'admin']

new_users = ['nigGa228', 'Bob', 'Maria', 'elize', 'tom']

for user in new_users:
    if user.lower() in curret_users:
        print('o hell nah ' + user)
    else:
        print('u good ' + user)
