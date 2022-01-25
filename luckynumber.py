import sys
givennumbers = sys.argv[1]
intlist = [int(x) for x in givennumbers.split(",") if int(x) >= 0]
checknumber = 1
editintlist = intlist[:]
newlist = []
if editintlist[0] == 1:
    for term in editintlist:
        if term%2 == 1:
            newlist.append(term)
else:
    for cunot in range(0, len(editintlist),2):
        newlist.append(editintlist[cunot])
        
        
while newlist[checknumber] <= len(newlist)+1:
    counter = 0
    while counter+newlist[checknumber]-1 < len(newlist):
        newlist.pop(counter+newlist[checknumber]-1)         
        counter = counter+newlist[checknumber]-1    
    checknumber = checknumber+1
       
for number in newlist:
    print(number, end=" ")