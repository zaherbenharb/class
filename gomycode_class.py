#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[41]:


class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        


# In[42]:


my_point= Point3D(1,2,3)


# In[43]:


print("point is a {},{},{}".format(my_point.x,my_point.y,my_point.z))


# In[52]:


class rectangle :
    def __init__(self,longeur,largeur):
        self.longeur = longeur
        self.largeur = largeur
    def aire(self,longeur,largeur):
        return longeur*largeur
    def périmètre(self,longeur,largeur):
        return (longeur+largeur)*2


# In[45]:





# In[46]:





# In[58]:


my_rectangle = rectangle(3,4)


# In[59]:


print(my_rectangle.périmètre(3,4))


# In[48]:


print("myrectangle de périmètre est : {}".format(périmètre(my_rectangle,3,4)))


# In[49]:


print("l'aire de myrectangle est  {}".format(aire(my_rectangle,3,4)))


# In[74]:


import math
class cercle :
    def __init__(self,O,r):
        self.O=O
        self.r=r
    def aire(self,O,r):
        return PI*r*r
    def périmètre(self,O,r):
        return PI*r*2
    def isinside(self,x,y):
        if math.sqrt(x**2+y**2)<self.r :
            print("isinside")
        else : 
            print("isoutside") 


# In[76]:


cercle2=cercle(0,16)
cercle2.isinside(0,7)


# In[80]:


class bank:
    def __init__(self,solde):
        self.solde=solde
    def dépot(self,soldedéposer):
        self.solde=self.solde+soldedéposer
        return self.solde
        
    def retrait(self,solderetirer):
            self.solde=self.solde-solderetirer
            return self.solde


# In[81]:


zaher=bank(4000)
zaher.dépot(500)


# In[82]:


zaher.retrait(700)


# In[ ]:




