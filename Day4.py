# In how many assignment pairs does one range fully contain the other?

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
            all_section_one_in_two = False
            if section not in second_coverage:
                break
            else:
                all_section_one_in_two = True
                
        for section in second_coverage:
            all_section_two_in_one = False
            if section not in first_coverage:
                break
            else:
                all_section_two_in_one = True
        
        if all_section_one_in_two or all_section_two_in_one:
            total += 1
            
print(total)