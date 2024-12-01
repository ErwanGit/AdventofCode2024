def import_data(name_fic, sort = False):
    try:
        fic = open(name_fic, 'r')
        fic.readline()

        list_num1 = []
        list_num2 = []
        for line in fic:
            [num1, num2] = line.split(',')
            list_num1.append(int(num1))
            list_num2.append(int(num2))

        fic.close()

        if sort:
            return (sorted(list_num1), sorted(list_num2))
        return (list_num1, list_num2)
    except:
        print('Error Import Data')
        return ([], [])
    
def occur_numbers(list):
    dict_occur_numbers = dict()
    for number in list:
        if number in dict_occur_numbers:
            dict_occur_numbers[number] += 1
        else:
            dict_occur_numbers[number] = 1
    return dict_occur_numbers
