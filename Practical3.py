


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
    if type(value) == dict:
        for k1, v1 in value.items():
            type_dict[k1] = type(v1)
    else:
        type_dict[key] = type(value)  #type_dict[] - означає додати ключ
print(type_dict)
