def file_reverser(file):
    with open(file) as f:
        file_ = f.readlines()

    file_ = [j[:-2] for j in file_][::-1]
    lines  = [j[::-1]+'\n' for j in file_]


    with open('file_name.txt', 'w') as f:
        f.writelines(lines)


file_reverser('x.txt')