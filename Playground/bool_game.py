import random


def create_bool(old, deep, level):
    new = ""
    bools = ["True", "False"]
    signs = ["==", "!="]
    first_bracket = ["", "("]
    first = random.choice(first_bracket)
    second = ""
    beginn_sign = ""
    if first == "(":
        second = ")"
    if old == "":
        beginn_sign = ""
    else:
        beginn_sign = random.choice(signs)
    new = old + beginn_sign + first + random.choice(bools) + random.choice(
        signs) + random.choice(bools) + second
    if deep < level:
        new = create_bool(new, deep+1, level)
    return new


for i in range(0, 5):
    bool_string = create_bool("", 0, i)
    user_choice = input(
        bool_string + "\n1) True\n2) False\n")
    user_bool = ""
    if user_choice == "1":
        user_bool = "True"
    elif user_choice == "2":
        user_bool = "False"
    if user_bool != str(eval(bool_string)):
        print("Failed!")
        exit()

print("Everything Correct!")
