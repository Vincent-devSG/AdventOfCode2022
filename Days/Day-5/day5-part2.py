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

    for i in range(len(copy)):
        for j in range(len(copy[i])):
            if copy[i][0] == ' ':
                copy[i].pop(0)
    crates = []
    for i in range(9):
        crates.append(Crates([]))

    length = 0
    for i in range(len(copy)):
        length = len(copy[i])
        for j in range(0, length):
            crates[i].stack.append(copy[i][length - 1 - j])

    for i in range(len(crates)):
        print(crates[i].stack)

    operations = []
    for i in range(10, 514):
        f[i] = f[i].replace('move ', '')
        f[i] = f[i].replace('from ', '')
        f[i] = f[i].replace('to ', '')
        f[i] = f[i].strip()
        operations.append(f[i])

    nb = []
    buffer = ''
    for i in range(len(operations)):
        for j in range(len(operations[i])):
            if operations[i][j] != ' ':
                buffer += operations[i][j]
                if j == len(operations[i]) - 1:
                    nb.append(buffer)
                    buffer = ''
            else:
                nb.append(buffer)
                buffer = ''

    count = 0
    sum = 0
    from_ = 0
    to_ = 0

    buffer = []

    for i in range(len(nb)):
        count += 1
        if count == 1:
            sum = int(nb[i])
        elif count == 2:
            from_ = int(nb[i]) - 1
        elif count == 3:
            count = 0
            to_ = int(nb[i]) - 1
            for j in range(sum):
                buffer.append(crates[from_].stack.pop(len(crates[from_].stack) - 1))
            for y in range(len(buffer)):
                crates[to_].stack.append(buffer[len(buffer) - 1 - y])
            buffer = []

    result = ''
    print('It becomes then: ')
    for i in range(len(crates)):
        print(crates[i].stack)
        result += crates[i].stack[len(crates[i].stack) - 1]

    print(result)


if __name__ == "__main__":
    main()
