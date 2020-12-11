fi=open("input7.txt","r")
txt=fi.read()
txt=txt.replace(".","").replace(" bags","").replace(" bag","")
Lines=txt.splitlines()
fi.close()

#acquisizione regole
Rules=[]
for line in Lines:
    temp=line.split(" contain ")
    rule={"name":temp[0], "bags_inside":[[int(x[0]), x[2:]] for x in temp[1].split(", ") if x<>"no other"]}
    Rules.append(rule)

def num_inside_bags(s):
    Bags=[]
    for rule in Rules:
        if rule["name"]==s:
            Bags=rule["bags_inside"][:]
    n=0
    for x in Bags:
        n+=x[0]*(1+num_inside_bags(x[1]))
    return n

print num_inside_bags("shiny gold")
    
