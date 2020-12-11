fi=open("input11.txt", "r")
txt=fi.read()
fi.close()
Lines=txt.splitlines()
matrix=[[x for x in Lines[i]] for i in range(len(Lines))]

def adj_seats(i, j):
    nc=len(matrix[0])
    nr=len(matrix)
    n0=[matrix[a][j] for a in range(i)]
    n0.reverse()
    s0=[matrix[a][j] for a in range(i+1,nr)]
    o0=matrix[i][:j]
    o0.reverse()
    e0=matrix[i][j+1:]
    #print n0, s0,o0, e0
    se0=[matrix [i+a][j+a] for a in range(1,min(nr-i-1, nc-j-1)+1)]
    no0=[matrix [i-a][j-a] for a in range(1,min(i, j)+1)]
    so0=[matrix [i+a][j-a] for a in range(1,min(nr-i-1, j)+1)]
    ne0=[matrix [i-a][j+a] for a in range(1,min(i, nc-j-1)+1)]
    #print no0, ne0, so0, se0
    n=[x for x in n0 if x<>"."]
    s=[x for x in s0 if x<>"."]
    e=[x for x in e0 if x<>"."]
    o=[x for x in o0 if x<>"."]
    no=[x for x in no0 if x<>"."]
    ne=[x for x in ne0 if x<>"."]
    se=[x for x in se0 if x<>"."]
    so=[x for x in so0 if x<>"."]
    return [len(n) and n[0], len(s) and s[0], len(e) and e[0], len(o) and o[0], len(se) and se[0], len(no) and no[0], len(so) and so[0], len(ne) and ne[0]]
                    
cicla=True           

while cicla:
    temp_matrix=[x[:] for x in matrix]
    for i in range(len(matrix)): #numero riga
        for j in range(len(matrix[0])): #numero colonna
            if matrix[i][j]=="L" and ("#" not in adj_seats(i,j)):
                temp_matrix[i][j]="#"
            elif matrix[i][j]=="#" and (adj_seats(i,j).count("#")>=5):
                temp_matrix[i][j]="L"
    if temp_matrix==matrix:
        cicla=False
    else:
        matrix=[x[:] for x in temp_matrix]
        
occupied=sum([x.count("#") for x in matrix])
print occupied


        


