import re


def main():
    f = open("Assignment.txt").readlines()
    list_assi = []
    score = 0

    for line in f:
        line = line.strip()
        line = re.findall(r"[\w']+", line)
        for elem in range(len(line)):
            line[elem] = int(line[elem])
        list_assi.append(line)

    for elem in range(len(list_assi)):
        if (list_assi[elem][0] <= list_assi[elem][2] and list_assi[elem][1] >= list_assi[elem][3]) or (
                list_assi[elem][2] <= list_assi[elem][0] and list_assi[elem][3] >= list_assi[elem][1]):

            score += 1

        print(list_assi[elem][0], '    into    ', list_assi[elem][2], '    ', list_assi[elem][1], '    into    ',
              list_assi[elem][3], ' SCORE IS : ', score)

    print(score)


if __name__ == "__main__":
    main()
