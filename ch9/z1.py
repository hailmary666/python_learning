class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nRestaurant name is " + self.restaurant_name.title() + ".")
        print("Cuisine type in this restaurant - " +
              self.cuisine_type + ".")

    def open_restaurant(self):
        print("Restaurant '" + self.restaurant_name.title() + "' is open")

restaurant = Restaurant('tomato', 'italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant('kopatich', 'russian')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('allah', 'uzbek')
restaurant3.describe_restaurant()
