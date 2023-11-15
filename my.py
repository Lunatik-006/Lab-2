from csv import reader
import xml.dom.minidom as minidom
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

#3
flag=1
output = open('result.txt', 'w')
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        if row[0][0]=='3' and flag<21:
            output.write(f'{flag}) {row[2]}. {row[1]} - {row[3]}\n')
            flag+=1
output.close()

#4
xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()
dom = minidom.parseString(xml_data)
dom.normalize()
elements = dom.getElementsByTagName('Valute')
names_dict = {}

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'Name':
                if child.firstChild.nodeType == 3:
                    name = child.firstChild.data
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3:
                    charcode = child.firstChild.data
    names_dict[name] = charcode
for key in names_dict.keys():
    print(key, names_dict[key])
print(names_dict)
xml_file.close()