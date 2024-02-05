def my_generator(start, end):
    while (start <= end):
        yield start
        start += 1

for i in my_generator(1, 3):
        print(i)