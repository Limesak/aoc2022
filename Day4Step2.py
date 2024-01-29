# In how many assignment pairs do the ranges overlap?

total = 0

with open("CleaningAssignments.txt", "r") as f:
    for pair in f:
        first_coverage = []
        second_coverage = []
        sep = pair.replace("-", ",").split(",")
        i = 0
        for i in range(int(sep[0]), int(sep[1]) + 1):
            first_coverage.append(i)
        for i in range(int(sep[2]), int(sep[3]) + 1):
            second_coverage.append(i)
        
        for section in first_coverage:
            if any(compared_section == section for compared_section in second_coverage):
                total += 1
                break
            
print(total)