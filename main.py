

from testz import *

a = Technic('zaa', 500, True)
b = Technic('kakk', 100, True)

if a.price < 100:
    print('Бюджетный')
else:
    print('Дорогой')
print(a<b)
