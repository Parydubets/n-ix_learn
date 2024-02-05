import sys

#cmd arguments variant
if len(sys.argv) == 3:
    print('Hello, {} {}! Nice to see you here!'.format(sys.argv[1], sys.argv[2]))
#stdin variant
else:
    for line in sys.stdin:
        if 'q' == line.rstrip():
            break
        line = sys.argv[1]+' '+line if len(sys.argv) == 2 else line
        print('Hello, {}! Nice to see you here!'.format(line.strip()))