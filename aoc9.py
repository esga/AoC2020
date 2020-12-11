fi=open("input9.txt", "r")
txt=fi.read()
fi.close()

numbers=[int(x) for x in txt.splitlines()]
outlier=0

#pt1
for i in range(len(numbers)-25):
    preamble=numbers[i:i+25]
    if int(numbers[i+25]) not in [preamble[a]+preamble[b] for a in range(25) for b in range(a) ]:
        outlier=numbers[i+25]
        break
print "pt 1: ", outlier


#pt2
for i in range(len(numbers)):
    j=2
    while sum(numbers[i:i+j])<outlier:
        j+=1
    if sum(numbers[i:i+j])==outlier:
        break
lista=numbers[i:i+j]
print "pt 2: ",max(lista)+min(lista)
        
