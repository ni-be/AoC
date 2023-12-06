with open('01.txt', 'r') as f:
    floor = 0
    count = 0
    for char in f.read():
        if char == '(':
            floor += 1
            count += 1

        elif char == ')':
            floor -= 1
            count += 1

        if floor == -1:
            print(count)
