a = 'Hello world!'
name ='Maxym'
surname = 'Bogulskyi'
age = 17
#print('Value а:', a, 'Type:', type(a))
#print('Value name:', name, 'Type:', type(name))
#print('Value surname:', surname, 'Type:', type(surname))
#print('Value age:', age,'Type:', type(age))
lst = [a, name, surname, age] # Список змінних
lst1 = [] #Значення змінних  
lst2 = [] #Типи змінні
string = [] #змінні з str
floatt = [] # float
intt = [] # int
for item in lst:
     lst1.append(item) #додаю значення змінних в lst1
     lst2.append(type(item)) #додаю типи змінних із lst в lst2
     if item == str:
          string.append(item)# якщо змінна типу стр додаю в список lst3
     elif item == int:
          intt.append(item)
     elif item == float:
          floatt.append(item)
if len(string) > len(floatt) and len(string) > len(intt):
     print('Більше значень із типом str')
elif len(floatt) > len(string) and len(floatt) > len(intt):
     print('Більше значень із типом float')
else:
     print('Більше значень із типом int')
print (lst2)
print (lst1)
