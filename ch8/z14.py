def make_car(manufacturer, car_name, **other_inf):
    car_inf = {}
    car_inf['manufacturer'] = manufacturer
    car_inf['car_name'] = car_name
    for key, value in other_inf.items():
        car_inf[key] = value
    return car_inf

car = make_car('subaru', 'x5',
               price = 'one million',
               color = 'red',
               )
print(car)
