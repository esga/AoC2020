def pt1():
    commands="7,12,1,0,16,2".split(",")
    numbers={int(x):[0,commands.index(str(x))+1] for x in commands}
    if "0" not in commands:
        numbers[0]=[0,0]
    n=int(commands[-1])
    for i in range(len(commands)+1,2021):
        if numbers[n][0]==0:
            n=0
        else:
            n_temp=i-1-numbers[n][0]
            n=n_temp 
        if n not in numbers.keys():
            numbers[n]=[0,i]
        else:
            numbers[n]=[numbers[n][1],i]    
    print n


def pt2():
    commands="7,12,1,0,16,2".split(",")
    numbers={int(x):[0,commands.index(str(x))+1] for x in commands}
    if "0" not in commands:
        numbers[0]=[0,0]
    n=int(commands[-1])
    for i in range(len(commands)+1,30000001):
        if numbers[n][0]==0:
            n=0
        else:
            n_temp=i-1-numbers[n][0]
            n=n_temp 
        if n not in numbers.keys():
            numbers[n]=[0,i]
        else:
            numbers[n]=[numbers[n][1],i]    
    print n

pt1()
