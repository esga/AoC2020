fi=open("input5.txt", "r")
text=fi.read()
Tickets=text.split('\n')
fi.close()

def seat_id(ticket):
    row=0
    column=0
    for i in range(0,7):
        if ticket[i]=="B":
            row+=2**(6-i)
    for i in range(0,3):
        if ticket[-3:][i]=="R":
            column+=2**(2-i)
    return row*8+column

Ids=[r*8+c for r in range(0,128) for c in range(0,8)]
for ticket in Tickets:
    Ids.remove(seat_id(ticket))

print Ids
    
    
