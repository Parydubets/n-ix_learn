import os


in_file_name = "input.txt"
out_file_name = "output"

def remove_duplicate_rows(in_file_name, out_file_name):
    out = open(out_file_name, 'w')
    unique = set()
    for line in open(in_file_name, 'r'):
        if line not in unique:
            unique.add(line)
            out.write(line)


def add_file_to_end(in_file_name, out_file_name):
    buf = open(in_file_name, 'r').readlines()
    open(out_file_name, 'a').writelines(buf)


def split_by_100(in_file_name, out_file_name):
    input = open(in_file_name, 'r')
    lines = input.readlines()
    n = 0
    while n in range(len(lines)):
        with open((out_file_name+"{}.txt".format(int(n/100))), 'a') as file:
            file.writelines(lines[n:n+100])
        n += 100


def print_first_30(in_file_name):
    with open(in_file_name) as file:
        print(file.readlines()[0:30])


def print_last_30(in_file_name):
    with open(in_file_name) as file:
        print(file.readlines()[-31:-1])

def print_start():
    with open("./tmp/file.txt") as file:
        print(file.read())


def print_file_with_test():
    with os.scandir('./') as entries:
        for entry in entries:
            if ".txt" in entry.name:
                with open(entry, 'r') as file:
                    if "test" in file.read():
                        print("'test' is in the '{}' file".format(entry.name))


print_file_with_test()