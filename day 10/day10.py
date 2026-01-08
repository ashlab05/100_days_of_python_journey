import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


result = 0

print(art.logo)
while True:
    operation = input("What do you want to do? +,*,-,/ : ")
    if input("Do you want to use previous result here? y/n: ") == "y":
        n1 = result
    else:
        n1 = int(input("Enter a number: "))

    n2 = int(input("Enter another number: "))

    ops = {
        "+": add(n1, n2),
        "-": subtract(n1, n2),
        "*": multiply(n1, n2),
        "/": divide(n1, n2),
    }

    result = ops[operation]

    print("The answer is ", result)
    if input("Do you want to continue? y/n: ") == "n":
        break
