#!/usr/bin/env python
# coding: utf-8

# Web sraping using python

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[68]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[69]:


page= requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[60]:


page


# In[71]:


Soup=BeautifulSoup(page.content)
Soup


# In[74]:


header=Soup.find('h2',class_="mp-h2")


# In[75]:


header


# In[76]:


header.text


# In[77]:


header=[]

for i in Soup.find_all('h2',class_="mp-h2"):
    header.append(i.text)


# In[78]:


header


# In[79]:


print(len(header))


# In[80]:


df=pd.DataFrame({'Header':header})


# In[81]:


df


# In[ ]:




