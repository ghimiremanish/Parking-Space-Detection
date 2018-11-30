
c = loadCo()

points = c.output()

# data manupulating to array
b = ''

#for storing stings
val = []
# final array list of polygon 
arr = []

#count
c = 0

for p in points:
    #rrmoving impurities from text to get numbers
    if p != '[' and p != '(' and p != ',' and p != ')' and p != ' ' and p != ']':
        val.append(p)

for i in val:
    b = b + i
    c = c + 1
    if c == 3:
        arr.append(int(b))
        b = ''
        c = 0
       

print(arr)