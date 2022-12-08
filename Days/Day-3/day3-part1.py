def main():
    alphabet = []

    for i in range(97, 123):
        alphabet.append([chr(i), i - 96])
    for i in range(65, 91):
        alphabet.append([chr(i), i - 38])

    words = []
    right = []
    left = []
    common_letters = []
    score = 0
    f = open("Rucksack.txt").readlines()

    for line in f:
        line = line.strip()
        words.append(line)

    for i in range(len(words)):
        left.append(words[i][:len(words[i]) // 2])
        right.append(words[i][len(words[i]) // 2:])

    for i in range(len(words)):
        common_letters.append(''.join(
            set(left[i]).intersection(right[i]))
        )

    for elem in common_letters:
        for i in range(len(alphabet)):
            if elem == alphabet[i][0]:
                score += alphabet[i][1]
                break

    print(score)


if __name__ == "__main__":
    main()
