m =  'my name is manish'
arr = [[1,2,3],[2,3,4],[3,4,5]]


f = open('m.txt', 'a')


for data in arr:
    f.write(str(data)+',')

