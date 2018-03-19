#-*- coding: utf-8 -*-

import string

def template(x, y, z):
    tmp = string.Template('$x時の$yは$z')
    return tmp.safe_substitute(x=str(x), y=str(y), z=str(z))

x = 12
y = '気温'
z = 22.4

print(template(x, y, z))
