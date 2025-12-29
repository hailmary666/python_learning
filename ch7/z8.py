sandwich_orders = ['hyunya', 'zalupa', 'jopa', 'pastrami', 'pastrami', 'pastrami']

print("We dont have pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print("I made your " + sandwich + " sandwich")

finished_sandwiches = []

while sandwich_orders:
    finished = sandwich_orders.pop()
    finished_sandwiches.append(finished)

for finished in finished_sandwiches:
    print("\n" + finished.title() + " sandwich is finished")
