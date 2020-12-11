

def read_passport(s):
    '''input stringa rappr passaporto, output diz passaporto'''
    passport=dict()
    for field in s.split(" "):
        if field:
            passport[field[0:3]]=field[4:]
    return passport
        
    

    
def passport_valid(psp):
    ''' input dizionario che rappresenta pass, output valido/no'''
    return ((len(psp)==8) or ((len(psp)==7) and ("cid" not in psp.keys())))


fi=open("input4.txt", "r")
valids=0
Lines=fi.readlines()
s=""
fi.close()
for line in Lines:
    if line!="\n":
        s+=line.replace("\n", " ") #ottengo linea ben formattata
        
    else:
        valids+=passport_valid(read_passport(s)) #aumenta contatore
        s="" #torno a stringa vuota
print(valids)
