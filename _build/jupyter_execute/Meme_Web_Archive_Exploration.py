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


get_ipython().system('pip install langdetect')

import pandas as pd
import matplotlib.pyplot as plt
#from IPython.core.display import display,HTML
from IPython.display import Image,display
from langdetect import detect
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')
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
# We can count the **length** of our data frame to see how many entries we have using thing len() function.
# 

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
meme_option = "Slowpoke" #@param {type:"string"}

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

# ## Language info
# 
# As we've seen in our examples there are many different languages represented in our dataset. Let's see if we can **enrich** our dataset by automatically detecting what language it is and adding that as a new column. We'll us the [langdetect](https://pypi.org/project/langdetect/) library to do this. 

# In[10]:


#Let's look at our random item again
rando


# In[11]:


# Let's the language of the random entry from earlier
# We'll get a two letter languge code that represents one of the languages in the list of ISO 639-1 codes (https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). 
detect(str(rando["Alternate Text"]))


# It would take to long to calculate all these values now for all of the entries in the dataset. So the next cell will just add a new column to our dataset of pre-calculated values.
# 
# 
# (It took 8 minutes for the code to run)

# In[12]:


#open CSV to dataframe
lang_data = pd.read_csv("https://raw.githubusercontent.com/BrockDSL/Analyzing_Web_Archives/main/language_data.csv")
#append to meme_data dataframe
meme_data = meme_data.join(lang_data)
meme_data.sample(5)


# In[13]:


language_count = dict()

# Go through each row of the data and see what two letter language code
# is in the iso_language_code metadata field

for row in meme_data.itertuples(index=False):
  language_entry = row[-1]
  #Create a lookup 'dictionary' of codes
  if language_entry in language_count:
    language_count[language_entry] += 1
  else:
    language_count[language_entry] = 1
    

plt.pie(list(language_count.values()),labels=list(language_count.keys()))
plt.title("Languages in the Memes")
plt.show()

