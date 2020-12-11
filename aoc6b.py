fi=open("input6.txt","r")
fileinput=fi.read()
fi.close()
Gruppi=fileinput.split("\n\n")

s=0
for gruppo in Gruppi:
    oggetti_dichiarazione=set([x for x in gruppo])
    Componenti=gruppo.split("\n")
    for persona in Componenti:
        oggetti_pers=set([x for x in persona])
        oggetti_dichiarazione=oggetti_dichiarazione.intersection(oggetti_pers)
    s+=len(oggetti_dichiarazione)

print s
