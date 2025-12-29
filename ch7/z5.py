prompt = ("What is your age? ")

age = input(prompt)
age = int(age)

if age < 3:
    print("free")
elif age <= 12:
    print("$10")
elif age > 12:
    print("$15")
