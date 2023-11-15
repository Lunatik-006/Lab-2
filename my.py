from csv import reader
#1
print(len([1 for i in open('books-en.csv').readlines() if len(i.split(';')[1])>30]))
#2
flag = 0
search = input('Enter book author: ')
output=[]
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        if row[0]!='ISBN':
            lower_case = row[2].lower()
            index = lower_case.find(search.lower())
            if index != -1:
                try:
                    year=int(row[3])
                    if year>=2018:
                        output.append(row[2])
                        flag = 1
                except: None
    if flag == 0:
        print('Nothing found.')
    else:
        for i in set(output):
            print(i)
