def import_data(name_fic):
        fic = open(name_fic, 'r')

        list = []
        for line in fic:
            lineNumbers = []
            numbers = line.split(' ')
            for number in numbers:
                lineNumbers.append(int(number))
            list.append(lineNumbers)

        fic.close()
        return list
    
def is_increasing(list_numbers):
    cpt_increasing = 0
    cpt_decreasing = 0

    for i in range(1, len(list_numbers)):
        if list_numbers[i] - list_numbers[i - 1] > 0:
            cpt_increasing += 1
        else:
            cpt_decreasing += 1
    
    return cpt_increasing >= cpt_decreasing