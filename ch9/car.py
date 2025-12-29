class Car():
    """Simple car model"""
    def __init__(self, make, model, year):
        """Initialising describe car atributs"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Givin back good format inf"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Probeg"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set new value on odometer.
        Block reverse value on odometer.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can`t roll back an odometer!")

    def increment_odometer(self, miles):
        """Incriese odometer value with followng incriese"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can`t do this shit")

    def fill_gas_tank(self):
        print("Filling gas right now")


