
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np 
#load the constituent funds 
df1 = pd.read_csv('C:/Users/nsw26/Desktop/Test_Merge/testmerge1.csv')
df2 = pd.read_csv('C:/Users/nsw26/Desktop/Test_Merge/testmerge2.csv')
#simple AUM - basically assumes share count also is AUM e.g. all shares are valued at $1 forever
sum1=df1.sum()
sum2=df2.sum()
df = df2.merge(df1,left_on='Stock',right_on='Stock',how='outer')
print(df)
print(sum1)
print(sum2)


# In[33]:


TotalABCFund1 = df1['Shares'].sum()
print(TotalABCFund1)


# In[41]:


#for ranking formula, the ranks of the funds are inverse 
ranktestmerge1 = 2
ranktestmerge2 = 1

#step4a position ranks, interim step, relative just to the stocks own portfolio
rankdf = ranktestmerge1/(df1['Shares']/sum1)


# In[54]:


Bottom1=df1['Shares']/50
#I had to manually enter 50, but I want this to be sum1 
#this takes each member of the shares and divides by AUM 


# # print(Bottom1)

# In[56]:


Top1=ranktestmerge2/Bottom1 
# this takes the rank divided by the step above 


# In[57]:


print(Top1)


# In[59]:


Bottom2=df2['Shares']/35
Top2=ranktestmerge1/Bottom2
print(Top2)


# In[60]:


combined = sum(Top1,Top2)


# In[61]:


print(combined)


# In[62]:


total=combined.sum()


# In[63]:


print(total)


# In[64]:


final=combined/total


# In[65]:


print(final)


# In[66]:


#check
sum(final)

