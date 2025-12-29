class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("\nRestaurant name is " + self.restaurant_name.title() + ".")
        print("Cuisine type in this restaurant - " +
              self.cuisine_type + "."
              )

    def served(self):
        print("Served " + str(self.number_served) + " persons.")

    def open_restaurant(self):
        print("Restaurant '" + self.restaurant_name.title() + "' is open")

    def set_number_served(self, new_n):
        self.number_served = new_n

    def increment_num_serv(self, inc_n):
        self.number_served += inc_n

restaurant = Restaurant('tomato', 'italian')
restaurant.set_number_served(10)
restaurant.increment_num_serv(20)
restaurant.describe_restaurant()
restaurant.served()
restaurant.open_restaurant()
