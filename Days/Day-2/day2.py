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

        match me:
            case 'X':
                if opp == 'C':
                    score += rock + win
                elif opp == 'A':
                    score += rock + draw
                else:
                    score += rock

            case 'Y':
                if opp == 'A':
                    score += paper + win
                elif opp == 'B':
                    score += paper + draw
                else:
                    score += paper

            case 'Z':
                if opp == 'B':
                    score += scissors + win
                elif opp == 'C':
                    score += scissors + draw
                else:
                    score += scissors
        print(me, ' VS ', opp, "   result: ", score)
    print(score)

if __name__ == "__main__":
    main()
