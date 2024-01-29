# Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

total_sum_of_priorities = 0

def AddToTotalSum(object_to_sort):
    if object_to_sort.isupper(): object_priority = ord(object_to_sort) - 38
    else: object_priority = ord(object_to_sort) - 96
    return object_priority

group = []

with open("RuckSacksToSort.txt", "r") as written_file:
    for sack in written_file:
        group.append(sack.strip())
        if len(group) == 3:
            badge = ''.join(set(group[0]) & set(group[1]) & set(group[2]))
            total_sum_of_priorities += AddToTotalSum(badge)
            group = []

print(total_sum_of_priorities)