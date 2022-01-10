#!/usr/bin/env python
# coding: utf-8

# ![dsl_logo.png](https://raw.githubusercontent.com/BrockDSL/Analyzing_Web_Archives/main/dsl_logo.png)
# 
# # Analyzing Web Archives
# 
# Welcome to the Digital Scholarship Lab Level Analyzing Web Archives workshop. The following notebook provides an investigation into the [Meme Generator dataset](https://www.loc.gov/item/2018655320/)
# 
# 
# ## How this notebook works
# 
# This webpage is a Google Colab notebook and is comprised of different *cells*. Some are code cells that run Python snippets. To works through these cells simply click on the triangle _run_ button in each cell. Click in the cell below to see the play button, then click on it.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
#from IPython.core.display import display,HTML
from IPython.display import Image,display

print("Libraries loaded, and ready to run!")


# # Loading our data set
# 
# The information from this archive is saved in a _CSV_ file. Or put in otherwords, something like a spreadsheet. In the next cell we will load this file into something call a dataframe and we'll look at the first 5 entries by looking at the **head**.

# In[2]:


meme_data = pd.read_csv("https://raw.githubusercontent.com/BrockDSL/Analyzing_Web_Archives/main/memegenerator.csv", sep=",")
meme_data.head(5)


# # Some General Data Exploration
# 
# 
# 
# 
# ---
# 
# 

# ### How much data?
# 
# We can count the **length** of our data frame to see how many entries we have

# In[3]:



print("We have this many memes to look at: ",len(meme_data))


# ### Random Entry
# 
# To get a better sense of what is in our dataset let's look at a random entry by using **sample** with a value of 1. Click the below button a few times to get a few different options.

# In[4]:


rando = meme_data.sample(1)
display(Image(url=rando['Archived URL'].values[0], format='jpg'))
print("View on Memegenerator: \t",rando['Meme Page URL'].values[0])
print("View on Archive: \t\t\t",rando['Archived URL'].values[0])
rando


# **Q1** Have a look at the data that is associated with a random record. In the chat box suggest some things you might want to explore with this data? Share your reponse in the chat box.

# 

# # Category of memes?
# 
# As you might know, memes come in many different flavours. Let's see if we can find out how many types there are? We'll do this by **grouping** our _Base Meme Name_ column and **counting** how many entries are in each.

# In[5]:


meme_data.groupby(["Base Meme Name"]).count()


# **Q2** Based on the above summary how many different type so memes we have? Share your response in the chat box.

# 

# Yikes! That looks like a lot. Let's just keep the top **25** entries. We'll do this by **sorting**.

# In[6]:


meme_data.groupby(["Base Meme Name"]).count().sort_values(by="Meme ID",ascending=False)[0:25]


# In[7]:


#@title Random Meme by Category
#@markdown Type copy and pasting one of the **Base Meme Name** to see a random entry from that category of meme
meme_option = "10guy" #@param {type:"string"}

rando = meme_data[meme_data["Base Meme Name"] == str(meme_option)].sample(1)
display(Image(url=rando['Archived URL'].values[0], format='jpg'))
print("View on Memegenerator: \t",rando['Meme Page URL'].values[0])
print("View on Archive: \t\t\t",rando['Archived URL'].values[0])
rando


# What's the **average** number of memes in each type?
# 
# 

# In[8]:


meme_type_average = meme_data.groupby(["Base Meme Name"])["Meme ID"].count().mean()
print("Average number of entries per meme category: ",meme_type_average)


# Let's draw a **histogram** of this distribution

# In[9]:


bins = 150

plt.hist(meme_data.groupby(["Base Meme Name"]).count().sort_values(by="Meme ID",ascending=False)["Meme ID"],bins)

plt.title("Category Frequency")
plt.xlabel("Number of Entries")
plt.ylabel("Number of Categories")
plt.show()


# **Q3** Can you describe this graph? What is the biggest value that it is showing?

# 

# data things to do
# - alt text somehow?
# - language detection?
# - pull in scores via API?
