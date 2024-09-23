


dictionary = { 'name': 'Maxym',
            'age': 17,
            'dict': {'1': 'tipchik',
                    '2': 'xz',
                    '3': 3.14,
                    '4': False,
                    '5': True}, 
            'python': 'piton',
            }
print(dictionary)


type_dict = {}  
for key, value in dictionary.items():
    type_dict[key] = type(value)  #type_dict[] - означає додати ключ
print(type_dict)
