class User():

    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        print("\nFirst name - " + self.first_name.title() +
              "\nLast name - " + self.last_name.title() +
              "\nAge - " + str(self.age)+
              "\nSex - " + self.sex
              )

    def greet_user(self):
        print("\nHello " + self.first_name.title() + "!")
        print("_________________________________________________")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('ilya', 'koznov', 22, 'male')
user1.describe_user()
user1.greet_user()

user2 = User('muhammed', 'ali', 12, 'male')
user2.describe_user()
user2.greet_user()

user3 = User('sweet', 'pussy', 18, 'female')
user3.describe_user()
user3.greet_user()
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
print("Loging attempts = " + str(user3.login_attempts))
user3.reset_login_attempts()
print("Loging attempts = " + str(user3.login_attempts))
