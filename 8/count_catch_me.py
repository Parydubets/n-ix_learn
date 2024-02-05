with open('input', 'r') as f:
    catch_me = []
    all = f.readlines()
    catch_me = list(filter(lambda line: 'catch me' in line, all))
    print(len(catch_me))