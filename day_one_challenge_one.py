with open('numbers.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = int(lines[i].strip())

    total_increased = 0

    for i in range(1, len(lines)):
        if lines[i] > lines[i-1]:
            total_increased +=1
    
    print(total_increased)
