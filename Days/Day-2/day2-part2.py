def main():
    my_hand = []
    opp_hand = []
    f = open("List_Hands.txt").readlines()

    rock = 1            #X for me A for opp
    paper = 2           #Y for me B for opp
    scissors = 3        #Z for me C for opp

    loss = 0
    draw = 3
    win = 6

    score = 0

    for line in f:
        line = line.split()
        opp_hand.append(line[0])
        my_hand.append(line[1])

    for hands in range(len(my_hand)):
        opp = opp_hand[hands]
        me = my_hand[hands]

        match opp:
            case 'A':
                if me == 'X':
                    score += scissors
                elif me == 'Y':
                    score += rock + draw
                else:
                    score += paper + win

            case 'B':
                if me == 'X':
                    score += rock
                elif me == 'Y':
                    score += paper + draw
                else:
                    score += scissors + win

            case 'C':
                if me == 'X':
                    score += paper
                elif me == 'Y':
                    score += scissors + draw
                else:
                    score += rock + win
    print(score)

if __name__ == "__main__":
    main()
