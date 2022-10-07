def name_file():
    name = []
    z = '0'
    print('Введите название файлов, для окончания введите 999')
    while True:
        z = input()
        if z == '999':
            break
        name.append(z)

    max = 0
    for i in name:
        maxi = len(i)
        if maxi > max:
            max = maxi
        
    for i in name:
        if len(i) < max:
            index = name.index(i)
            i = i + ('_'*(max-len(i)))
            name[index] = i
    return(name)
