fi=open("input14.txt", "r")
text=fi.read()
#text="mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\nmem[8] = 11\nmem[7] = 101\nmem[8] = 0"
commands=[(x[:x.find("=")-1],x[x.find("=")+2:]) for x in text.splitlines()]

def base2(n):
    a=str(bin(n)[2:])
    return "0"*(36-len(a))+a

def base10(s):
    return int(s,2)



def pt1():
    memory=dict()
    mask=""
    for c in commands:
        if c[0]=="mask":
            mask=c[1]
        else:
            indn=int(c[0][4:-1])
            n=int(c[1])
            n2=base2(n)
            change=False
            for i in range(0,36):
                if mask[i]=="0" and n2[i]=="1":
                    n2=n2[:i]+"0"+n2[i+1:]
                    change=True
                if mask[i]=="1" and n2[i]=="0":
                    n2=n2[:i]+"1"+n2[i+1:]
                    change=True
                
            #print mask,"\n", n2,change
            memory[indn]=base10(n2)
    print "pt1: ", sum(memory.values())



def modify_bitpt2(strind, mask):
    if not strind:
        return [""]
    elif mask[0]=="0":
        return [strind[0]+s for s in modify_bitpt2(strind[1:], mask[1:])]
    elif mask[0]=="1":
        return ["1"+s for s in modify_bitpt2(strind[1:], mask[1:])]
    elif mask[0]=="X":
        return ["0"+s for s in modify_bitpt2(strind[1:], mask[1:])]+["1"+s for s in modify_bitpt2(strind[1:], mask[1:])]
    return 0

def pt2():
    memory=dict()
    mask=""
    for c in commands:
        if c[0]=="mask":
            mask=c[1]
        else:
            indn=int(c[0][4:-1])
            n=int(c[1])
            indn2=base2(indn)
            index=modify_bitpt2(indn2, mask)
            for i in index:
                memory[i]=n
    print "pt2: ", sum(memory.values())      

pt1()
pt2()
