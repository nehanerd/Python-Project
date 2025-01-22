# Program is a four function calculator

def main():
    numone = int(input('Enter a number:'))
    numtwo = int(input('Enter another number:'))
    sign = input("These are the four operators you can do add, subtract, multiply, or divide."
                 " Type A,S,M,D respectively: ")
    ans = 0
    if sign == 'A':
        ans = addition(numone, numtwo)
    elif sign == 'S':
        ans = subtraction(numone, numtwo)
    elif sign == 'M':
        ans = multiplication(numone, numtwo)
    elif sign == 'D':
        ans = division(numone, numtwo)
    print("The answer is", ans)


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    cq = int(input("Press 1, if you want (first number - second number), else press 2: "))
    if cq == 1:
        return num1 - num2
    return num2 - num1


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    cq = int(input("Press 1, if you want (first number / second number), else press 2: "))
    if cq == 1:
        return num1 / num2
    return num2 / num1


main()
