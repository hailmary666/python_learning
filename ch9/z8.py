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


class Privileges():
    def __init__(self):
        self.privileges = ['can that', 'also can that', 'and dont forget about that']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):

    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = Privileges()
    

