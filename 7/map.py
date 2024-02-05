def hello_country(users_list):
    if users_list[1]=='ru':
        return 'Привет, %s!'%users_list[0]
    elif users_list[1] == 'us':
        return 'Hello, %s!'%users_list[0]
    elif users_list[1] == 'es':
        return 'Hola, %s!'%users_list[0]
    else:
        return 'Hello, %s, but I do not know where are you from!'%users_list[0]

users_list = [
    ('Александр', 'ru'),
    ('James', 'us'),
    ('Daniella', 'es'),
    ('Someone', 'unknown country'),
]

print(list(map(hello_country, users_list)))