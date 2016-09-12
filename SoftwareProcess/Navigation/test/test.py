'''
    Created on Sep 11, 2016
    @author: Donghuang Li
'''
import __init__.Angle as Angle

a = Angle()
a.setDegrees(-299.5)
b = Angle()
b.setDegreesAndMinutes("60d20")
print a.compare(b)
a.subtract(b)
print a.getString()
print a.getDegrees()