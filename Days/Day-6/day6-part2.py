def main():
    sentences = []
    letters = []
    solutions = ""
    count = 0
    tab_isIn = []
    f = open("code.txt").readlines()

    for line in f:
        sentences.append(line)

    for i in range(0, len(sentences[0])):
        count += 1
        if len(letters) != 14:
            letters.append(sentences[0][i])
            tab_isIn.append(True)
        else:
            del letters[0]
            letters.append(sentences[0][i])

            for j in range(len(letters)):
                if letters.count(letters[j]) > 1:
                    tab_isIn[j] = True
                else:
                    tab_isIn[j] = False
            print(letters)
            print(tab_isIn)
            if tab_isIn.count(True) == 0:
                solutions = letters[13]
                print(letters)
                break

    print(solutions, " after : ", count, " letters")



if __name__ == "__main__":
    main()
