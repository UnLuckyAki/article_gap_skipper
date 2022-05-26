with open("result.txt", 'w') as file:
    ancestor = open("ancestor.txt", "r")
    for line in ancestor.readlines():
        line = line.replace('\n',' ').replace('ML', 'machine learning').replace('DI','data integration')
        file.write(line)
