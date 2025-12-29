def city_country(city, country):

    inf = {}

    inf[country] = city

    for country, city in inf.items():
        print(country.title() + ", " + city.title())

add_city = input("Enter your city: ")
add_country = input("Enter your country: ")

city_country(add_city, add_country)
