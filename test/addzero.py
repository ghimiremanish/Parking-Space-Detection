point1 = (123,982)
point2 = (23,124)
point3 = (332,88)
point4 = (345,10)

data = [point1,point2,point3,point4]
for d in data:
    for c in d:
        if len(str(c)) == 2:
            v = '0' + str(c)
            
            print v


# print data
