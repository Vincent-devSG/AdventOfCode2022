from typing import List


class Elv:
    def __init__(self, food):
        self.food = food

    def get_sum(self):
        return sum(self.food)


def main():
    elv_food: list[int] = []
    elv_list = []
    f = open("List_Elvs.txt").readlines()
    f.append("\n")

    for line in f:
        if line != ('\n'):
            line = line.strip()
            elv_food.append(int(line))
        else:
            elv_list.append(Elv(elv_food))
            elv_food = []

    """""
    for i in range(len(elv_list)):
        print("i : ", i, "      sum: ", elv_list[i].get_sum(), "     list of food: ", elv_list[i].food)
    """

    max = 0
    for i in range(len(elv_list)):
        if elv_list[i].get_sum()>max:
            max = elv_list[i].get_sum()

    print(max)

if __name__ == "__main__":
    main()
