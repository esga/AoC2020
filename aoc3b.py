fi = open("input3.txt", "r")
Lines= fi.readlines()
fi.close()

lung=31
alte=len(Lines)
c=0
alberi=0
slope_r=1
slope_d=2

for i in range(0,alte,slope_d) :
    line=Lines[i]
    if line[c]=="#":
        alberi=alberi+1
    c=(c+slope_r)%31

print(alberi)

