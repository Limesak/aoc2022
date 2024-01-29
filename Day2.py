strategy_guide = "StrategyGuideRPS.txt"

def CheckHand(hand):
    if hand == "A" or hand == "X":
        return "rock"
    elif hand == "B" or hand == "Y":
        return "paper"
    elif hand == "C" or hand == "Z":
        return "scissors"

def AttributeScoreToHand(my_hand):
    if my_hand == "rock":
        return 1
    elif my_hand == "paper":
        return 2
    elif my_hand == "scissors":
        return 3

def CheckWinner(my_hand, elf_hand):
    win_points = 6
    draw_points = 3
    lose_points = 0
    
    if my_hand == elf_hand:
        return draw_points
    else:
        match my_hand:
            case "rock":
                if elf_hand == "paper":
                    return lose_points
                else:
                    return win_points
            case "paper":
                if elf_hand == "rock":
                    return win_points
                else:
                    return lose_points
            case "scissors":
                if elf_hand == "rock":
                    return lose_points
                else:
                    return win_points

with open(strategy_guide, "r") as written_file:
    my_total_score = 0
    rounds = written_file.readlines()
    for round in rounds:
        elf_hand = CheckHand(round[0])
        my_hand = CheckHand(round[2])
        score_of_round = CheckWinner(my_hand, elf_hand) + AttributeScoreToHand(my_hand)
        my_total_score += score_of_round
    print(f"My total score is {my_total_score}")