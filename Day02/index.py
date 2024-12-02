from functions import import_data, is_increasing

def part1():
    lists_numbers = import_data('input')

    cpt_safe = 0
    for list in lists_numbers:
        mode = 'increasing'
        if list[1] - list[0] < 0:
            mode = 'decreasing'

        i = 1
        invalid = False
        while i < len(list) and not invalid:
            diff = list[i] - list[i - 1]
            if diff < 0 and mode == 'decreasing' or diff > 0 and mode == 'increasing':
                if abs(diff) > 3:
                    invalid = True
            else:
                invalid = True
            i += 1

        if not invalid:
            cpt_safe += 1
    print(cpt_safe)

def part2():
    lists_numbers = import_data('input')

    cpt_safe = 0
    for list in lists_numbers:
        i = 1
        invalid = 0
        is_increase = is_increasing(list)
        while i < len(list) and invalid != 2:
            diff = list[i] - list[i - 1]
            if (diff < 0 and not is_increase) or (diff > 0 and is_increase):
                if abs(diff) > 3:
                    invalid += 1
                    list.pop(i)
                else: 
                    i += 1
            else:
                list.pop(i - 1)
                invalid += 1

        if invalid < 2:
            print(list)
            cpt_safe += 1
    print(cpt_safe)

part2()