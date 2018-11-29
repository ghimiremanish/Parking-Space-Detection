class loadCo:
    f = open('coordinates.txt', 'r')








c = loadCo()
print(type(c.f.read()))
result = map(int, c.f.read())
print(type(result))
print(result)
