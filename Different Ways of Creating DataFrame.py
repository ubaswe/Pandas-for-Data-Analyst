#Using csv file
import pandas as pd
df=pd.read_csv("data.csv")
df



#Using excel file
import pandas as pd
df=pd.read_excel("climate.xlsx","Sheet1")
df



#Using dictionary
climate_data ={
    "Day":["1/1/2023","1/2/2023","1/3/2023","1/4/2023"],
    "Temparature":[35,36,37,38],
    "Winspeed":[3,6,9,7],
    "Event":["rainy","sunny","rainy","sunny"] 
}
df=pd.DataFrame(climate_data)
df


#Using tuple list
climate_data=[
    (1/1/2023,35,3,"rainy"),
    (1/2/2023,35,3,"sunny"),
    (1/3/2023,35,3,"rainy"),
    (1/4/2023,35,3,"sunny")
]
df=pd.DataFrame(data=climate_data,columns=["Day","Temparature","weedspeed","Event"])
df



#Using list of dictionaries
climate_data = [
   {"Day":"1/1/2023","Temparature":35,"Windspeed":3,"Event":"rainy"},
   {"Day":"1/2/2023","Temparature":36,"Windspeed":3,"Event":"rainy"},
   {"Day":"1/3/2023","Temparature":37,"Windspeed":3,"Event":"rainy"},
   {"Day":"1/4/2023","Temparature":38,"Windspeed":3,"Event":"rainy"}
]
df=pd.DataFrame(data=climate_data,columns=["Day","Temparature","weedspeed","Event"])
df

#using clipboard
import pandas as pd
df=pd.read_clipboard()
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





