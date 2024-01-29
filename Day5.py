# After the rearrangement procedure completes, what crate ends up on top of each stack?

stack_one = ["N", "D", "M", "Q", "B", "P", "Z"] 
stack_two = ["C", "L", "Z", "Q", "M", "D", "H", "V"] 
stack_three = ["Q", "H", "R", "D", "V", "F", "Z", "G"] 
stack_four = ["H", "G", "D", "F", "N"] 
stack_five = ["N", "F", "Q"] 
stack_six = ["D", "Q", "V", "Z", "F", "B", "T"] 
stack_seven = ["Q", "M", "T", "Z", "D", "V", "S", "H"] 
stack_eight = ["M", "G", "F", "P", "N", "Q"] 
stack_nine = ["B", "W", "R", "M"] 

stacks = {
    1: stack_one,
    2: stack_two,
    3: stack_three,
    4: stack_four,
    5: stack_five,
    6: stack_six,
    7: stack_seven,
    8: stack_eight,
    9: stack_nine
    }

def MoveCrate(from_crate, to_crate):
    to_crate.append(from_crate[-1])
    from_crate.pop()

with open ("SupplyStacks.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if lines.index(line) >= 10:
            values = line.replace("move ", "").replace(" from ", "-").replace(" to ", "-").strip().split("-")
            quantity = int(values[0])
            origin = stacks[int(values[1])]
            destination = stacks[int(values[2])]
            for i in range(quantity):
                MoveCrate(origin, destination)

top_of_stacks = ""
for stack in stacks.values():
    top_of_stacks += stack[-1]
print(top_of_stacks)