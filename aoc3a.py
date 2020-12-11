fi = open("input3.txt", "r")
lung=31
Lines= fi.readlines()
c=0
alberi=0
slope_r=3

for line in Lines:
    if line[c]=="#":
        alberi=alberi+1
    c=(c+slope_r)%31

print(alberi)
    
fi.close()
