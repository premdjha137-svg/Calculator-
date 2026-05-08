#calculater
# calculator

while True:
    num1 = int(input("Any number: "))
    num2 = int(input("Any number: "))

    choose = input("Choose (+, -, *, /, %): ")

    if choose == "+":
        print(num1 + num2)
    elif choose == "-":
       print(num1 - num2)
    elif choose == "*":
        print(num1 * num2)
    elif choose == "/":
        print(num1/num2)
    elif choose =="%":
        print(num1%num2)
