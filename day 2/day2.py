# Data Types
# Subscripting
print("Hello"[0])

# String
print("123" + "345")

# Integer = Whole number
print(123 + 345)

# Large Integers
print(123_456_789)

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True)
print(False)

len("12345")

print(type(12345))
print(type("12345"))
print(type(123.45))
print(type(123.45 == 123.45))

# Conversion
print(int(123.45))
print(float(123))
print(str(123.45))

print("Number of letters in your name: " + str(len(input("Enter your name: "))))

print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(5 / 3)
print(5 // 3)
print(2**3)

# PEMDASLR Order
# ()
# **
# * OR /
# + OR -

# Outputs 7
print(3 * 3 + 3 / 3 - 3)

# Outputs 3
print(3 + 3 * 3 / 3 - 3)

bmi = 84 / 1.65**2

# Original Float with decimal places
print(bmi)

# Flooring the number by converting it into int
print(int(bmi))

# Rounding the number into a whole number
print(round(bmi))

# Rounding only to 2 decimal places
print(round(bmi, 2))


## Accumulate
score = 0

# User scores a point
score += 1
print(score)

# Also
score -= 1
score *= 2
score /= 2

score = 0
height = 1.8
is_winning = True

print(
    f"Your score is = {score}, your height is {height}. You are winning is {is_winning}"
)

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

amount = bill * tip / 100 + bill

print(f"Each person should pay: ${amount / people:.2f}")
