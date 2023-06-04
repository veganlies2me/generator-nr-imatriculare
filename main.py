import random
import string

def random_char(y):
       return ''.join(random.choice(string.ascii_uppercase) for x in range(y))

nrcetateni = ['B','AB','AG','AR','BC','BH','BN','BR','BT','BV','BZ','CJ','CL','CS','CT','CV','DB','DJ','GJ','GL','GR','HD','HR','IF','IL','IS','MH','MM','MS','NT','OT','PH','SB','SJ','SM','SV','TL','TM','TR','VL','VN','VS']
judet=random.choice(nrcetateni)
if judet == 'B':
    numar=random.randint(10,999)
else:
    numar=random.randint(10,99)
print(judet,numar,random_char(3))