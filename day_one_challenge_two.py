with open('numbers.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = int(lines[i].strip())

    total_increased = 0

    for i in range(3, len(lines)):
        if lines[i] + lines[i-1] + lines[i-2] > lines[i-1] + lines[i-2] + lines[i-3]:
            total_increased +=1
    
    print(total_increased)
