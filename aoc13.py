fi=open("input13.txt", "r")
txt=fi.read()
timestamp,text_bus=txt.splitlines()
timestamp=int(timestamp)
#text_bus="7,13,x,x,59,x,31,19"
str_bus=[n for n in text_bus.split(",")]
bus=[int(n) for n in text_bus.split(",") if n <>"x"]

def pt1():
    first_bus=[]
    for n in bus:
        first_bus.append(((timestamp/n)+1)*n) if timestamp%n<>0 else first_bus.append(timestamp)
    num_autobus=bus[first_bus.index(min(first_bus))]
    diff=min(first_bus)-timestamp
    return diff*num_autobus

def productlist(l):
    N=1
    for i in l:
        N*=i
    return N



def pt2(): #teorema cinese del resto
    b=[(-str_bus.index(str(i)))%i for i in bus]
    n=bus[:]
    N=productlist(n)
    Ni=[]
    for i in range(len(b)):
        temp_list=n[:]
        temp_list[i]=1
        Ni.append(productlist(temp_list))
    y=[0]*len(b)
    for i in range(len(b)):
        searchingy=True
        temp_y=0
        while searchingy and temp_y<=n[i]:
            if (temp_y*Ni[i])%n[i]==1:
                searchingy=False
                y[i]=temp_y
            else:
                temp_y+=1
    x0=sum([b[i]*Ni[i]*y[i] for i in range(len(n))])
    x=x0%N
    return x

print "pt1 :", pt1()
print "pt2: ", pt2()
Programmazionexpivelli.0
