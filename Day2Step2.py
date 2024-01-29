strategy_guide = "StrategyGuideRPS.txt"

def CheckStatus(status):
    win_points = 6
    draw_points = 3
    lose_points = 0
    match status:
        case "X":
            return lose_points
        case "Y":
            return draw_points
        case "Z":
            return win_points

def CheckElfHand(elf_hand):
    if elf_hand == "A":
        return "rock"
    elif elf_hand == "B":
        return "paper"
    elif elf_hand == "C":
        return "scissors"

def SignScore(elf_hand, instruction):
    match instruction:
        case 6:
            if elf_hand == "rock":
                return 2
            elif elf_hand == "paper":
                return 3
            elif elf_hand == "scissors":
                return 1
        case 3:
            if elf_hand == "rock":
                return 1
            elif elf_hand == "paper":
                return 2
            elif elf_hand == "scissors":
                return 3
        case 0:
            if elf_hand == "rock":
                return 3
            elif elf_hand == "paper":
                return 1
            elif elf_hand == "scissors":
                return 2

with open(strategy_guide, "r") as written_file:
    my_total_score = 0
    rounds = written_file.readlines()
    for round in rounds:
        elf_hand = CheckElfHand(round[0])
        my_instruction = CheckStatus(round[2])
        score_of_round = my_instruction + SignScore(elf_hand, my_instruction)
        my_total_score += score_of_round
    print(f"My total score is {my_total_score}")