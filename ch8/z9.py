def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    great_magicians = []
    for magician in magicians:
        great_magicians.append(magician + " the great")
    return great_magicians

magicians = ['bobby', 'maria']
result = make_great(magicians[:])

show_magicians(magicians)
show_magicians(result)
