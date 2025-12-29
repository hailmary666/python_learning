what = {'andrew': 'bad person',
        'niga': 'good person',
        'bob': 'strange person',
        }

for otvet in what:
    if otvet != 'bob':
        print(otvet.title() + " - " + what[otvet] + ";\n")
    else:
        print(otvet.title() + " - " + what[otvet] + ".")
