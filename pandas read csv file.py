#import pandas and read csv file 
import pandas as pd
df=pd.read_csv("data.csv")
df

#import pandas and read excel file
import pandas as pd
df=pd.read_excel("climate.xlsx","Sheet1")
df

#import pandas and read dictionary file
climate_data ={
    "Day":["1/1/2023","1/2/2023","1/3/2023","1/4/2023"],
    "Temparature":[35,36,37,38],
    "Winspeed":[3,6,9,7],
    "Event":["rainy","sunny","rainy","sunny"] 
}
df=pd.DataFrame(climate_data)
df






# In[2]:to print head rows
df.head()


# In[3]:to print tail rows
df.tail()


# In[4]:to print all columns
df.columns


# In[5]:to print specific column
df.Day


# In[7]:to print specific column
df.Event





