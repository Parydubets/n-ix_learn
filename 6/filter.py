list_ = [
    {'name': 'Alex', 'age': 25},
    {'name': 'Oleg', 'age': 23},
    {'name': 'Anna', 'age': 32},
    {'name': 'Igor', 'age': 50},
    {'name': 'Anton', 'age': 17},
]

print(list(filter(lambda x: (x['name'][0] == 'A' and 18 < x['age'] < 30), list_)))
