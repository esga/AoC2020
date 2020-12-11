fi=open("input7.txt","r")
txt=fi.read()
txt=txt.replace(".","").replace(" bags","").replace(" bag","")
Lines=txt.splitlines()
fi.close()

output_colors=set()
#acquisizione regole
Rules=[]
for line in Lines:
    temp=line.split(" contain ")
    rule={"name":temp[0], "bags_inside":[[int(x[0]), x[2:]] for x in temp[1].split(", ") if x<>"no other"]}
    Rules.append(rule)

    if "shiny gold" in [x[1] for x in rule["bags_inside"]]:
        output_colors.add(rule["name"])

new_colors=set(output_colors)

def bags_containing_this_color(s):
    Bags=set()
    for rule in Rules:
        if s in [x[1] for x in rule["bags_inside"]]:
            Bags.add(rule["name"])
    return Bags

while new_colors:
    temp_new_colors=set()
    for color in new_colors:
        temp_new_colors.update(bags_containing_this_color(color).difference(output_colors.union(new_colors)))
    new_colors=temp_new_colors
    output_colors.update(new_colors)

print len(output_colors)
