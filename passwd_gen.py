import random


def rand_pass():
    # This is going to generate a random 4 digits password
    string1 = ""
    string2 = []
    while len(string2) < 4:
        use = random.randint(0, 9)
        string2.append(use)
    for e in string2:
        string1 += str(e)
    print(string1)


rand_pass()