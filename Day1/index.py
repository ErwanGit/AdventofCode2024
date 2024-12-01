from functions import import_data, occur_numbers

name_fic = 'input.csv'

def part1():
    (list1, list2) = import_data(name_fic, True)

    cpt = 0
    for i in range(len(list1)):
        cpt += abs(list1[i] - list2[i])
    print(cpt)

def part2():
    (list1, list2) = import_data(name_fic)
    dict_occur_numbers = occur_numbers(list2)

    cpt = 0
    for i in range(len(list1)):
        occur_list2 = 0
        if list1[i] in dict_occur_numbers:
            occur_list2 = dict_occur_numbers[list1[i]]

        cpt += list1[i] * occur_list2
    print(cpt)


part1()
part2()