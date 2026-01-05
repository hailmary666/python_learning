"""classes for forming electrocars"""
from car import Car

class Battery():
    """simple battery model"""

    def upgrade_battery(self):
        """cheks razmer battery and set power = 85 if it have not 85 value"""
        if self.battery_size != 85:
            self.battery_size = 85

    def get_range(self):
        """show zapas hoda"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    
    def __init__(self, battery_size=70):
        """initialising battery atributs"""
        self.battery_size = battery_size
    def describe_battery(self):
        """show battery information"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
    """elctric car aspects"""
    def __init__(self, make, model, year):
        """
        initialising parent-class atributs
        after that initialising specific atributs for electrocar
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """electrocars have no gas tank"""
        print("This car doesn`t need a gas tank, you idiot!")

tesla = ElectricCar('tesla', 'x5', 2016)
tesla.battery.get_range()
tesla.battery.upgrade_battery()
tesla.battery.get_range()


