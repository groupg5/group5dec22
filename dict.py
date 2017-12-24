#!/usr/bin/python
#Author:murali
#purpose:using dictionary functions
n={'fname':'shanu','id':105960,'desg':'scpe'}

if(n.has_key('fname')):
    
 print 'key i s available'

else:
    
 print 'key is not available'

print n['fname']

del n['id']

print n

print n.keys()

print n.values()

n.clear()

print n

