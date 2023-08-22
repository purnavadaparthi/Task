#!/usr/bin/env python
# coding: utf-8

# In[1]:


#cost of the bike displays the road tax to be paid according tp the following criteria
#1
import time
from time import time
a=int(input('cost of the bike: '))
start = time()
if a>100000:
    print(f'{a} tax paid by the bike is 15%' )
elif a>50000 and a<=100000:
    print ( f'{a} tax paid by the bike is 10' )
elif a<=50000:
    print(f'{a} tax paid byb the bike is 5%')
else:
    print(f'{a} no tax paid')
end = time()
print(end-start)


# In[2]:


#2
import time
from time import time
a=int(input('cost of the bike: '))
start = time()
if a!=0:
    if a>=100000:
        print(f'{a} tax paid is 15%')
    elif a>=50000:
              print(f'{a} tax paid is 10%')
    else:
                    print(f'{a} no tax paid')
                    
else:
                    print(f'{a} no road tax to vehicle')
end = time()
print(end-start)
                      


# In[4]:


# 3
import time
from time import time
a=int(input('cost of the bike: '))
start = time()
b = 100000
c = 50000
if a>b:
    print('you have to pay 15% tax')
elif a>c and a<b:
    print('you have to pay 10% tax')
else:
    print('you dont have to pay 5% any tax')
end = time()
print(end-start)


# In[ ]:




