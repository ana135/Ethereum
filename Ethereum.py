#!/usr/bin/env python
# coding: utf-8

# In[1]:


5


# In[2]:


a=5


# In[9]:


# Matplotlibplot


# In[4]:


import matplotlib.pyplot as plt


# In[6]:


plt.plot([1,2,3,4,5])
plt.show()


# In[7]:


#MATPLOTLIBPLOT


# In[14]:


import pandas as pd


# In[16]:


import numpy as np


# In[17]:


import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[19]:


import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns 

df = pd.read_csv(r'C:\Users\a361097\Downloads\bnb_usd\BNB-USD.csv') 
df.head(3)


# In[20]:


df.info()


# In[21]:


df.describe()


# In[22]:


df = df.drop(['Adj Close'],axis=1)
df.head(2)


# In[23]:


#Create new columns as year, month day, and return 
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day 

df["Return"] = df["Close"]/ df["Open"][0]-1


# In[24]:


df.head(2)


# In[25]:


sns.pairplot(data=df, corner = True )


# In[34]:


#Create three lineplots 
f,ax = plt.subplots(3,1,figsize=(15,20))
sns.lineplot(data = df,ax =ax[0], x="Date",y="Open", color = "blue")
ax[0].legend(["Open"])
ax[0].set_title("Ethereum (2015~2018)",fontsize=22)
sns.lineplot(data=df, ax = ax[1], x="Date",y="Close",color="purple")
ax[1].legend(["Close"])
ax[1].set_title("Close")
sns.lineplot(data=df,ax=ax[2],x="Date", y="Volume",color = "yellow")
ax[2].legend(["Volume"])
ax[2].set_title("Volume ")

plt.show()


# In[ ]:





# In[27]:


sns.heatmap(df.corr())


# In[39]:


sns.lineplot(data = df,ax =ax[0], x="Date",y="Open", color = "blue")


# In[ ]:





# In[29]:


df2 = df.groupby('Date')[['Date','Open','High','Close','Low']].sum()
df2.head(4)
#A heat map (or heatmap) is a data visualization technique that shows magnitude of a phenomenon as color in two dimensions. 
#The variation in color may be by hue or intensity, giving obvious visual cues to the reader about how the phenomenon is clustered 
#or varies over space.


# In[1]:


#Predict trend, weekly, and yearly 
dis2 = m.plot_components(forecast)


# In[2]:


from fbprophet import Prophet 

#Predict date 
m = Prophet()
m.fit(df4)


# In[3]:





# In[ ]:




