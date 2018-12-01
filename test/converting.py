f = open('coordinates.txt','r')
v = f.read()
m = v.split()

print type(m)
print m
# results = [('1', '2', '3'),('1')]
# print type(results)
# result = map(int, results)
# print result