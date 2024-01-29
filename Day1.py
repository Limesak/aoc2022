most_calories = 0
second_most_calories = 0
third_most_calories = 0

def CurrentBag():
    bag = []
    elves_file = "ListOfElves.txt"
    with open(elves_file, "r") as writtenFile:
        lines = writtenFile.readlines()
        for line in lines:
            if line == "\n":
                RicherElf(sum(bag))
                bag.clear()
            else:
                bag.append(int(line))

def RicherElf(newSum):
    global most_calories
    global second_most_calories
    global third_most_calories
    if newSum > most_calories:
        most_calories = newSum
    elif newSum > second_most_calories:
        second_most_calories = newSum
    elif newSum > third_most_calories:
        third_most_calories = newSum

def DisplayRicherElf():
    print(f"The richest elf has {most_calories} calories")
    print(f"The top three elves have {most_calories}, {second_most_calories} and {third_most_calories} calories")
    print(f"The total of those three is {most_calories + second_most_calories + third_most_calories} calories")

CurrentBag()
DisplayRicherElf()