fi=open("input10.txt","r")
txt=fi.read()
jolts=[int(x) for x in txt.splitlines()]
fi.close()

sorted_jolts=jolts[:]
sorted_jolts.append(0)
sorted_jolts.sort()
sorted_jolts.append(sorted_jolts[-1]+3)
diff=[sorted_jolts[i+1]-sorted_jolts[i] for i in range(len(sorted_jolts)-1)]

count1=diff.count(1)
count3=diff.count(3)

print "pt 1: ", count1*count3

ways_to_get_there=[1]

for i in range(1, len(sorted_jolts)):
    s=0
    if diff[i-1]==1:
        s+=ways_to_get_there[i-1]
        if i-2>=0 and diff[i-2]==1:
            s+=ways_to_get_there[i-2]
            if i-3>=0 and diff[i-3]==1:
                s+=ways_to_get_there[i-3]
    else:
        s+=ways_to_get_there[i-1]
    ways_to_get_there.append(s)
    

print "pt 2: ", ways_to_get_there[-1]
