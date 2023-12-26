
# In[1]:


import pandas as pd
df=pd.read_excel("ResultGrade.xlsx","Sheet1")
df


# In[2]:add a column named total


df["Total"]=df["Math"]+df["English"]+df["Bangla"]+df["Science"]+df["History"]
df


# In[11]:add a column named Percentage
#add percentage.2


df["Percentage"]=(df["Total"]/500*100).apply("{:.2f}%".format)
df


# In[6]:add a column named Grade


df["Grade"]="None"
df

