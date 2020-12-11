fi=open("input5.txt", "r")
text=fi.read()
Tickets=text.split('\n')
fi.close()

def seat_info(ticket):
    row=0
    column=0
    for i in range(0,7):
        if ticket[i]=="B":
            row+=2**(6-i)
    for i in range(0,3):
        if ticket[-3:][i]=="R":
            column+=2**(2-i)
    return [row*8+column, row, column]

max_id=0
for ticket in Tickets:
    temp_id=seat_info(ticket)[0]
    if temp_id>max_id:
        max_id=temp_id

print max_id
    
    
