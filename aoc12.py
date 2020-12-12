fi=open("input12.txt", "r")
txt=fi.read()
Commands=[(x[0], int(x[1:])) for x in txt.splitlines()]

def pt1():
    ns=0
    eo=0
    rot=0
    for c in Commands:
        if c[0]=="N":
            ns+=c[1]
        elif c[0]=="S":
            ns-=c[1]
        elif c[0]=="E":
            eo+=c[1]
        elif c[0]=="W":
            eo-=c[1]
        elif c[0]=="L":
            rot=(rot+c[1])%360
        elif c[0]=="R":
            rot=(rot-c[1])%360
        elif c[0]=="F":
            if rot==0:
                eo+=c[1]
            elif rot==90:
                ns+=c[1]
            elif rot==180:
                eo-=c[1]
            elif rot==270:
                ns-=c[1]
    return abs(ns)+abs(eo)

def pt2():
    nsw=1
    eow=10
    ns=0
    eo=0
    for c in Commands:
        if c[0]=="N":
            nsw+=c[1]
        elif c[0]=="S":
            nsw-=c[1]
        elif c[0]=="E":
            eow+=c[1]
        elif c[0]=="W":
            eow-=c[1]
        elif c[0]=="L" or c[0]=="R":
            r=(c[1])%360 if c[0]=="L" else (-c[1])%360
            if r==90:
                nsw,eow=eow,-nsw
            if r==180:
                nsw,eow=-nsw,-eow
            if r==270:
                nsw,eow=-eow,nsw
        elif c[0]=="F":
            ns+=(c[1]*nsw)
            eo+=(c[1]*eow)
        #print nsw, eow, ns, eo
    return abs(ns)+abs(eo)

print "pt1: ", pt1()
print "pt2: ", pt2()

