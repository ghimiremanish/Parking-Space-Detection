# f = open('emp.txt','r')
import os
if  os.path.getsize('emp.txt') == 0:
    print 'empty'