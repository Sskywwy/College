a = 'Hello world!'
name ='Maxym'
surname = 'Bogulskyi'
age = 17
#print('Value а:', a, 'Type:', type(a))
#print('Value name:', name, 'Type:', type(name))
#print('Value surname:', surname, 'Type:', type(surname))
#print('Value age:', age,'Type:', type(age))
lst = [a, name, surname, age] # Список змінних
lst2 = []
lst3 = []
lst4 = []
for item in lst:
     lst2.append(type(item)) #додаю типи змінних із lst в lst2
     if item == str:
          lst3.append(item)# якщо змінна типу стр додаю в список lst3
     else:
          lst4.append(item)# якщо ні - lst4
if len(lst3) > len(lst4):
     print('Більше значень із типом str')
elif len(lst3) < len(lst4):
     print('Більше значень із типом int')
else:
     print('Однакові')
print (lst2)
