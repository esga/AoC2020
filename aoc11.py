fi=open("input11.txt", "r")
txt=fi.read()
fi.close()
Lines=txt.splitlines()
matrix=[[x for x in Lines[i]] for i in range(len(Lines))]

def adj_seats(i, j):
    adj=[]
    if i==0:
        if j==0:
            adj.extend([matrix[i][j+1], matrix[i+1][j+1], matrix[i+1][j]])
        elif j==len(matrix[0])-1:
            adj.extend([matrix[i][j-1], matrix[i+1][j-1], matrix[i+1][j]])
        else:
            adj.extend([matrix[i][j-1], matrix[i+1][j-1], matrix[i+1][j], matrix[i][j+1], matrix[i+1][j+1]])
    elif i==len(matrix)-1:
        if j==0:
            adj.extend([matrix[i][j+1], matrix[i-1][j+1], matrix[i-1][j]])
        elif j==len(matrix[0])-1:
            adj.extend([matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j]])
        else:
            adj.extend([matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j], matrix[i][j+1], matrix[i-1][j+1]])
    else:
        if j==0:
            adj.extend([matrix[i][j+1], matrix[i-1][j+1], matrix[i-1][j], matrix[i+1][j+1], matrix[i+1][j]])
        elif j==len(matrix[0])-1:
            adj.extend([matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j], matrix[i+1][j-1], matrix[i+1][j]])
        else:
            adj.extend([matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j], matrix[i][j+1], matrix[i-1][j+1], matrix[i+1][j-1], matrix[i+1][j], matrix[i+1][j+1]])
    return adj
        
            
finish=True

while finish:
    temp_matrix=[x[:] for x in matrix]
    for i in range(len(matrix)): #numero riga
        for j in range(len(matrix[0])): #numero colonna
            if matrix[i][j]=="L" and ("#" not in adj_seats(i,j)):
                temp_matrix[i][j]="#"
            elif matrix[i][j]=="#" and (adj_seats(i,j).count("#")>=4):
                temp_matrix[i][j]="L"
    if temp_matrix==matrix:
        finish=False
    else:
        matrix=[x[:] for x in temp_matrix]
        
occupied=sum([x.count("#") for x in matrix])
print occupied


        


