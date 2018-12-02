#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import csv
import numpy as np
import glob

data = numpy.asarray([])    
for filename in glob.glob('*.xlsx'):
    #file = 'sidi_boussaid.xlsx'
    xl = pd.ExcelFile(filename)
    #print(xl.sheet_names)
    try:
        df1 = xl.parse('الجباية المحلية')
        df = df1[df1['السنوات']==2016]
        tail=df.tail(1)
        total=tail['الإستخلاصات المستوجبة']
        print("Total: " + str(total))
        paid=tail['الاستخلاصات']
        print("Paid: " + str(paid))
        percentage=(paid/total)*100
        print("Percentage: " + str(percentage))
        print()
        t_uple=np.asarray([])
        t_uple=np.append(t_uple,filename)
        t_uple=np.append(t_uple,total)
        t_uple=np.append(t_uple,paid)
        data=np.append(data,t_uple)
    except Exception as e:
        print(e)
print(data)
numpy.savetxt("foo.csv", data, delimiter=",", fmt="%s", encoding='utf8')


# In[ ]:





# In[ ]:





# In[5]:





# In[46]:





# In[9]:





# In[42]:


df


# In[19]:





# In[20]:


tail


# In[25]:





# In[26]:


total


# In[27]:





# In[28]:


paid


# In[32]:





# In[33]:


percentage


# In[39]:


with open("result", 'wb', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(mylist)


# In[ ]:




