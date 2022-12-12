def main():
    sentences = []
    letters = []
    solutions = ""
    count = 0
    f = open("code.txt").readlines()

    for line in f:
        sentences.append(line)

    for i in range(0, len(sentences[0])):
        count += 1
        if len(letters) != 4:
            letters.append(sentences[0][i])
        else:
            del letters[0]
            letters.append(sentences[0][i])

            if letters[0] != letters[1] and letters[0] != letters[2] and letters[0] != letters[3] and letters[1] != \
                    letters[2] and letters[1] != letters[3] and letters[2] != letters[3]:
                solutions = letters[3]
                print(letters)
                break

    print(solutions, " after : ", count, " letters")


if __name__ == "__main__":
    main()
