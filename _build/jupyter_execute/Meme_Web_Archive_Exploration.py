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
# 
# ![How to](how-to.gif)

# In[1]:


get_ipython().system('pip install langdetect')
get_ipython().system('pip install pandas')

import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import Image,display,IFrame
from ipywidgets import widgets,interact,interact_manual
from langdetect import detect
import matplotlib.pyplot as plt

global rando

get_ipython().run_line_magic('matplotlib', 'inline')
print("\nLibraries loaded, and ready to run!")


# # Loading our data set
# 
# The information from this archive is saved in a _CSV_ file. Or put in otherwords, something like a spreadsheet. In the next cell we will load this file into something call a dataframe and we'll look at the first 5 entries by looking at the **head**.

# In[2]:


meme_data = pd.read_csv("https://raw.githubusercontent.com/BrockDSL/Analyzing_Web_Archives/main/memegenerator.csv", sep=",")
meme_data["Meme ID"] = meme_data["Meme ID"].astype(str)

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


#Random Entry Form
def show_random(choice):
  rando = meme_data[meme_data["Base Meme Name"] == str(choice)].sample(1)
  print("View on Memegenerator: \t",rando['Meme Page URL'].values[0])
  print("View on Archive: \t\t\t",rando['Archived URL'].values[0])
  display(Image(url=rando['Archived URL'].values[0], format='jpg'))
  display(rando)


title_textbox = widgets.Text(
    value='Me Gusta',
    description='Category',
)
print("Enter a meme category from the list above to see a random entry in that category")
print("Click 'Show' to display\n")
show_random_control = interact_manual.options(manual_name="Show")
show_random_control(show_random,choice=title_textbox);


# Let's know look at how the meme is displayed as a table

# What's the **average** number of memes in each type?
# 
# 

# In[8]:


meme_type_average = meme_data.groupby(["Base Meme Name"])["Meme ID"].count().mean()
print("Average number of entries per meme category: ",meme_type_average)


# The average might be a little misleading. Let's also check what the median number is for each base meme. The code chunk below is incomplete. Can you resolve the error?

# In[9]:


meme_type_median = meme_data.groupby(["Base Meme Name"])["Meme ID"].count().median()
print("The median number of entires per base meme is: ",meme_type_median)


# As you can see, the difference between the mean and the median is significant. This is because there's a skewed distribution in our dataset. Do you have any guesses as to why this might be the case? Share your thoughts in the chat!
# 
# Let's visualize this skewed distribution by drawing a **histogram**.

# In[10]:


bins = 150

plt.hist(meme_data.groupby(["Base Meme Name"]).count().sort_values(by="Meme ID",ascending=False)["Meme ID"],bins)

plt.title("Category Frequency")
plt.xlabel("Number of Entries")
plt.ylabel("Number of Categories")
plt.show()


# **Q3** Can you describe this graph? What is the biggest value that it is showing?

# ## Language info
# 
# As we've seen in our examples there are many different languages represented in our dataset. Let's see if we can **enrich** our dataset by automatically detecting what language it is and adding that as a new column. We'll use the [langdetect](https://pypi.org/project/langdetect/) library to do this. We can use the text in the _Alternate Text_ column.

# In[11]:


#Let's look at our random item again
rando


# In[12]:


# Let's the language of the random entry from earlier
# We'll get a two letter languge code that represents one of the languages in the list of ISO 639-1 codes (https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). 
print(detect(str(rando["Alternate Text"])))


# It would take to long to calculate all these values now for all of the entries in the dataset. So the next cell will just add a new column to our dataset of pre-calculated values. (It took 8 minutes for language detection code to run on the original dataset)
# 
# Have a look at the new column _Language_ that was added.

# In[13]:


#reload original dataset
meme_data = pd.read_csv("https://raw.githubusercontent.com/BrockDSL/Analyzing_Web_Archives/main/memegenerator.csv", sep=",")
meme_data["Meme ID"] = meme_data["Meme ID"].astype(str)

#open CSV of language info and create a dataframe
lang_data = pd.read_csv("https://raw.githubusercontent.com/BrockDSL/Analyzing_Web_Archives/main/language_data.csv")

#language data from to meme_data dataframe
meme_data = meme_data.join(lang_data)
meme_data.sample(5)


# 
# ## Summary of Language Information?
# 
# Run the next cell to generate a pie graph of the language count in the meme.

# In[14]:


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


# That's a lot of languages!

# ## Meme Scores!
# 
# Memegenerator has voting capability. By clicking the up or down arrow users can increase / descrease this score. Let's see this for our random meme. Run the next cell to generate the preview

# In[15]:


preview_url = str(rando['Meme Page URL'].values[0])
preview_url = preview_url.replace("http:","https:")

IFrame(preview_url,width=1000, height=700)


# To enrich our dataset even more we found the scores of all of the memes in dataset. We did this by **downloading** all 60000 meme webpages and screen scrapping to find the score that was presented on the page. This took about **4 Hours** so we won't recreate this here. We will however open a CSV file of these scores and add them to our dataset, just like we did with the language information. Run the next cell to do this and preview a few random scores.

# In[16]:


#Lets open the file and have a peak.
meme_scores = pd.read_csv("https://raw.githubusercontent.com/BrockDSL/Analyzing_Web_Archives/main/meme_scores.csv",dtype={'Meme ID': object})
meme_scores["Meme ID"] = meme_scores["Meme ID"].astype(str)
meme_scores.sample(5)


# Let's add this data to our original dataset by matching on the **Meme ID** column. Then let's look at a couple of random entries of our newly enriched completed dataset. For memes that we couldn't get a score for, we use a placeholder valued called _NaN_. (We missed some scores because the memes were deleted from the website) Run the next cell to create our final version of the dataset with all of enriched data and display a few random entries. Notice how we add a column called _Score_.
# 

# In[17]:


#Original Dataset
meme_data = pd.read_csv("https://raw.githubusercontent.com/BrockDSL/Analyzing_Web_Archives/main/memegenerator.csv", sep=",")
meme_data["Meme ID"] = meme_data["Meme ID"].astype(str)

#Language information added
lang_data = pd.read_csv("https://raw.githubusercontent.com/BrockDSL/Analyzing_Web_Archives/main/language_data.csv")
meme_data = meme_data.join(lang_data)

#Meme Score Added
meme_scores = pd.read_csv("https://raw.githubusercontent.com/BrockDSL/Analyzing_Web_Archives/main/meme_scores.csv",dtype={'Meme ID': object})
meme_scores["Meme ID"] = meme_scores["Meme ID"].astype(str)
meme_data = pd.merge(meme_data,meme_scores,on="Meme ID", how = "outer")
meme_data.dropna(thresh=8,inplace=True)

#set our random item to be from our new dataframe
rando = meme_data.sample(1)
meme_data.sample(5)


# ## The Final Analysis: Scores
# 
# 
# Let's take a look at some aspects of our data now that we have enriched it with all the extra pieces:
# 
# - Language 
# - Scores

# In[18]:


print("Average score of memes: ",meme_data["Score"].mean())


# 

# In[19]:


print("Average score by languages, top 10 only: ")
pd.DataFrame(meme_data.groupby("Language").mean()["Score"].sort_values(ascending=False)[0:10])


# In[20]:


print("Average score by base memes, top 25 only: ")
#print(meme_data.groupby("Base Meme Name").mean()["Score"].sort_values(ascending=False)[0:25])
pd.DataFrame(meme_data.groupby("Base Meme Name").mean()["Score"].sort_values(ascending=False)[0:25])


# ## Highest Scoring Meme in the dataset!

# In[21]:


display(Image(url=meme_data[meme_data['Score'] == meme_data['Score'].max()]['Archived URL'].values[0], format='jpg'))
meme_data[meme_data['Score'] == meme_data['Score'].max()]


# 
# # Congratulations
# 
# You've now had a tour of the Memegenerator dataset and found some interesting results.
