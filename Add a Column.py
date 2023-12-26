#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_excel("ResultGrade.xlsx","Sheet1")
df


# In[2]:


df["Total"]=df["Math"]+df["English"]+df["Bangla"]+df["Science"]+df["History"]
df


# In[11]:


df["Percentage"]=(df["Total"]/500*100).apply("{:.2f}%".format)
df


# In[6]:


df["Grade"]="None"
df

