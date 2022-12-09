class Elv:
    def __init__(self, shit):
        self.shit = shit

    def get_sum(self):
        return sum(self.shit)


def main():

    f = open("Rucksack.txt").readlines()

    alphabet = []
    for i in range(97, 123):
        alphabet.append([chr(i), i - 96])
    for i in range(65, 91):
        alphabet.append([chr(i), i - 38])

    words = []
    common_letters = []
    stack_elv = []
    buffer = []
    score = 0

    for line in f:
        line = line.strip()
        words.append(line)

        if len(words) == 3:
            stack_elv.append(Elv(words))
            words = []

    for i in range(len(stack_elv)):
        buffer.append(''.join(
            set(stack_elv[i].shit[0]).intersection(stack_elv[i].shit[1]))
        )
        common_letters.append(''.join(
            set(stack_elv[i].shit[2]).intersection(buffer[0]))
        )
        buffer = []

    for elem in common_letters:
        for i in range(len(alphabet)):
            if elem == alphabet[i][0]:
                score += alphabet[i][1]
                break

    print(score)


if __name__ == "__main__":
    main()
