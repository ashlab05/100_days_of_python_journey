# Random
import random

heads_or_tails = random.randint(1, 3)
if heads_or_tails == 1:
    print("Heads")
else:
    print("Tails")

# Lists concepts
states_of_america = [
    "Delaware",
    "Pennsylvania",
    "New Jersey",
    "Georgia",
    "Connecticut",
    "Massachusetts",
    "Maryland",
    "South Carolina",
    "New Hampshire",
    "Virginia",
    "New York",
    "North Carolina",
    "Rhode Island",
    "Vermont",
    "Kentucky",
    "Tennessee",
    "Ohio",
    "Louisiana",
    "Indiana",
    "Mississippi",
    "Illinois",
    "Alabama",
    "Maine",
    "Missouri",
    "Arkansas",
    "Michigan",
    "Florida",
    "Texas",
    "Iowa",
    "Wisconsin",
    "California",
    "Minnesota",
    "Oregon",
    "Kansas",
    "West Virginia",
    "Nevada",
    "Nebraska",
    "Colorado",
    "North Dakota",
    "South Dakota",
    "Montana",
    "Washington",
    "Idaho",
    "Wyoming",
    "Utah",
    "Oklahoma",
    "New Mexico",
    "Arizona",
    "Alaska",
    "Hawaii",
]

states_of_america[1] = "Pencilvania"

states_of_america.append("Angelaland")

states_of_america.extend(["Angelaland", "Jack Bauer Land"])

print(states_of_america)

# Who has to pay

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(f"The one who has to pay is {random.choice(friends)}")

# Rock paper Scissors
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
user_choice = int(input("Enter your choice: Rock(0)/Paper(1)/Scissors(2): "))

print("Computer chose:\n", options[computer_choice])
print("User chose:\n", options[user_choice])

if user_choice == computer_choice:
    print("Draw")
else:
    if (
        (user_choice == 0 and computer_choice == 2)
        or (user_choice == 1 and computer_choice == 0)
        or (user_choice == 2 and computer_choice == 1)
    ):
        print("You win")
    else:
        print("You lose")
