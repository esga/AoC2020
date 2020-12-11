fi=open("input8.txt","r")
txt=fi.read()
fi.close()
Lines=txt.splitlines()
Initial_Instructions=[(line[0:3], int(line[4:])) for line in Lines]

def run_instructions(Instructions):
    already_computed=set()
    acc=0
    i=0
    while i not in already_computed and i<len(Instructions):
        already_computed.add(i)
        if Instructions[i][0]=="nop":
            i+=1
        elif Instructions[i][0]=="acc":
            acc+=Instructions[i][1]
            i+=1
        else:
            i+=Instructions[i][1]
    return [i,acc]
		
def part2(Instructions):
    n=len(Instructions)
    for i in range(n):
        if Instructions[i][0]=="nop":
            New_instr=Instructions[:]
            New_instr[i]=("jmp", Instructions[i][1])
            val=run_instructions(New_instr)
            if val[0]==n:
                return val
        elif Instructions[i][0]=="jmp":
            New_instr=Instructions[:]
            New_instr[i]=("nop", Instructions[i][1])
            val=run_instructions(New_instr)
            if val[0]==n:
                return val
    return [0,0]

pt1=run_instructions(Initial_Instructions)
print "part1: ", pt1[1]
pt2=part2(Initial_Instructions)
print "part2: ", pt2[1]        
