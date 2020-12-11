fi=open("input6.txt","r")
fileinput=fi.read()
Gruppi=fileinput.split("\n\n")

s=0
for gruppo in Gruppi:
    gruppo=gruppo.replace("\n", "")
    oggetti=set([x for x in gruppo])
    s+=len(oggetti)

print s
    
