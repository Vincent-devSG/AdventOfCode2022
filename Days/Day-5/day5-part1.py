class Crates:
    def __init__(self, stack):
        self.stack = stack


def main():
    rows = []
    f = open("Crates.txt").readlines()
    c = False
    suppr = []
    copy = []

    for i in range(9):
        f[i] = f[i].rstrip()
        f[i] = f[i].replace('[', ' ')
        f[i] = f[i].replace(']', ' ')
        # f[i] = list(f[i].split(" "))
        rows.append(f[i])

    column = [[] for i in range(0, 35)]

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            column[j].append(rows[i][j])

    for i in range(len(column)):
        c = False
        for j in range(len(column[i])):
            if column[i][j] != " ":
                c = True
        if c:
            suppr.append(i)

    for i in range(len(column)):
        if suppr.count(i) > 0:
            copy.append(column[i])

    ' '.join(copy[0]).split()

    for i in range(len(copy)):
        print(copy[i], sep='\n')


if __name__ == "__main__":
    main()
