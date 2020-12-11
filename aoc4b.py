def read_passport(s):
    '''input stringa rappr passaporto, output diz passaporto'''
    passport=dict()
    for field in s.split(" "):
        if field:
            passport[field[0:3]]=field[4:]
    return passport

def isnum(string):
    return set(string).issubset(set("1234567890"))

def isesa(string):
    return set(string).issubset(set("1234567890abcdef"))

def passport_valid(psp):
    ''' input dizionario che rappresenta pass, output valido/no'''
    return ((len(psp)==8) or ((len(psp)==7) and ("cid" not in psp.keys())))

def valid_byr(psp):
    return len(psp["byr"])==4 and 1920<=int(psp["byr"])<=2002

def valid_iyr(psp):
    print(psp["iyr"])
    print len(psp["iyr"])==4 and 2010<=int(psp["iyr"])<=2020
    return len(psp["iyr"])==4 and 2010<=int(psp["iyr"])<=2020

def valid_eyr(psp):
    return len(psp["eyr"])==4 and 2020<=int(psp["eyr"])<=2030

def valid_hgt(psp):
    unit=psp["hgt"][-2:]
    number=psp["hgt"][0:-2]
    if unit=="cm" and isnum(number):
        return 150<=int(number)<=193
    if unit=="in" and isnum(number):
        return 59<=int(number)<=76
    return False

def valid_hcl(psp):
    return len(psp["hcl"])==7 and psp["hcl"][0]=="#" and isesa(psp["hcl"][1:])

def valid_ecl(psp):
    return psp["ecl"] in ["amb", "blu","brn","gry","grn","hzl","oth"]

def valid_pid(psp):
    return len(psp["pid"])==9
    


fi=open("input4.txt", "r")
valids=0
Lines=fi.readlines()
s=""
fi.close()
for line in Lines:
    if line!="\n":
        s+=line.replace("\n", " ") #ottengo linea ben formattata
        
    else:
        psp=read_passport(s)
        if passport_valid(psp): #se il passaporto e' valido
            valids+=(valid_byr(psp) and valid_iyr(psp) and valid_eyr(psp) and valid_hgt(psp) and valid_hcl(psp) and valid_ecl(psp) and valid_pid(psp))
        s="" #torno a stringa vuota
print(valids)
