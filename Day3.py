# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

total_sum_of_priorities = 0

def AddToTotalSum(object_to_sort):
    if object_to_sort.isupper(): object_priority = ord(object_to_sort) - 38
    else: object_priority = ord(object_to_sort) - 96
    return object_priority

with open("RuckSacksToSort.txt", "r") as written_file:
    for sack in written_file:
        first_half = sack[:len(sack)//2]
        second_half = sack[len(sack)//2:]
        commonItems = ''.join(set(first_half).intersection(second_half))
        total_sum_of_priorities += AddToTotalSum(commonItems)

print(total_sum_of_priorities)