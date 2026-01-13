number = ("Type number:")
number += ("\n(Type 'q' to quit) ")
process = ("Type process:")
process += ("\n(+, -, *, /) ")
number2 =("Type 2 number: ")
x = input(number)
if x == 'q':
    quit()
while True:
    pr = input(process)
    if pr == 'q':
        break
    elif pr not in ('+', '-', '*', '/'):
        print("Invalid operator. Please try again.")
        continue
    y = input(number2)
    if y == 'q':
        break
    ans = int(x)
    if pr == '+':
        ans += int(y)
    elif pr == '-':
        ans -= int(y)
    elif pr == '*':
        ans *= int(y)
    elif pr == '/':
        if y == '0':
            print("You can't divide by zero!")
            continue
        else:   
            ans /= int(y)
    print (f"The answer is: {ans}")
    question = input("You want continue calculating with the answer?(y/n):")
    if question == 'n':
        break
    elif question == 'y':
        x = ans
    else:
        print("Invalid input. Exiting the calculator.")
        break