# создание словаря из имеющихся файлов
text = {}
for i in range(1, 4):
    file_name = str(i) + '.txt'
    file = open(file_name, 'rt', encoding='utf-8')
    text[file_name] = file.readlines()
    file.close()

#обнуление имеющегося файла
    file = open('result.txt', 'w')
    file.close()

#запись файла из отсортированного по длине значений словаря. Как проще?
for key, val in dict((sorted(text.items(), key=lambda item: len(item[1])))).items():
    with open('result.txt', 'a', encoding='utf8') as file:
        file.writelines(f'{key}\n')
        file.write(f'{str(len(val))}\n')
        for i in range(len(val)):
            file.writelines(val[i])
        file.write('\n')
