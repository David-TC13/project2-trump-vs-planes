#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib


# In[2]:


import warnings
warnings.filterwarnings("ignore")


# ## Obtaning the df. about 

# In[3]:


df_suicide = pd.read_csv('data/master.csv')


# In[4]:


df_suicide.sample()


# In[5]:


df_suicide.country.unique() # checking if United Kingdom is included in the list of countries of the DF


# ### Cleaning data in order to get the suicide rates from 2005 in the United Kingdom to see the pre and post retransmission of Love Island

# In[6]:


import src.cleaning as clean


# In[7]:


df_suicide = clean.cl_colm(df_suicide) # cleaning columns


# In[8]:


df_suicide_uk = clean.cl_country_year_null(df_suicide) # cleaning countries, years<2004 and null values


# In[9]:


df_suicide_uk.sample()


# ## Obtaining via web scraping the releases Love Island until 2020

# In[10]:


import src.scrp as sc


# ### Getting the info from Love Island 

# In[11]:


url='https://thetvdb.com/series/love-island/allseasons/official'


# In[12]:


soup = sc.extrc(url) # Importing all the info from the website


# In[13]:


love_island_date = soup.find_all("ul", attrs={'class':'list-inline text-muted'}) # Getting the dates of each episode
love_island_date[1]


# ### Cleaning the data for the dates

# In[14]:


lst_date= sc.clearance_date(love_island_date)


# In[15]:


lst_date[2]


# In[16]:


year= sc.def_year(lst_date)
year[1]


# In[17]:


month= sc.def_month(lst_date)
month[0]


# ### Getting the data of seasons and episodes

# In[18]:


love_island_episode= soup.find_all("span", attrs={'class':'text-muted'}) # Getting the list of episodes with seasons
love_island_episode[10]


# In[19]:


import src.scrp_epis as sc2


# In[20]:


season_episode = sc2.episode_season(love_island_episode) #split the season and episodes


# In[21]:


lst_episodes = sc2.episodes(season_episode) # creating a list of episodes to include in a new DF


# In[22]:


lst_seasons = sc2.episodes(season_episode)# creating a list of seasons linked with episodes to include in a new DF


# ### Creating a DF with all the data above

# In[23]:


import src.loveislanddf as lidf


# In[24]:


love_island_dict=lidf.dictionary(lst_seasons,lst_episodes,year,month) # defining a dictionary of lists


# In[25]:


df_loveisland_until_2020= lidf.dfloveisland (love_island_dict) # defining the dictionary


# In[26]:


df_loveisland_until_2020.sample()


# ## Analysis

# ### checking the information can be related with both DF, in this cas, the years

# In[27]:


import src.groupby as gb


# In[28]:


df_loveisland_until_2020.Season.unique()


# In[29]:


df_suicide_uk.sample()


# In[30]:


df_suicide_uk.year.unique()


# In[31]:


df_suicide_ages = gb.group_suici_age (df_suicide_uk) # Group by ages and years the suicide rates
df_suicide_ages


# In[32]:


df_distr_epi = gb.group_season_epi (df_loveisland_until_2020)
df_distr_epi


# ## Figures for suicide

# - As can be check of the graph below the ages in between 16-34 years old have a raise on the suicide rates

# In[33]:


suicide_ages = sns.lineplot(data=df_suicide_ages, x="year", y="suicides_no", hue="age").set(title="Suicide no. from 2005-2020");


# In[34]:


# suicide_ages.figure.savefig("age_suic.jpg", dpi=1000)


# ## Figures for Love island

# In[35]:


epis_year = sns.barplot(data=df_loveisland_until_2020, x="Year", y="Episode", estimator="count", ci=None).set(title="Episodes by season");


# In[36]:


# epis_year.figure.savefig("epis_years.jpg", dpi=1000)


# ## Getting all the graphs together

# ### Join the DF by the year

# In[37]:


df_suicide_uk.sample()


# In[38]:


import src.joining as jn


# In[39]:


df_join= jn.join_df(df_suicide_uk, df_loveisland_until_2020)# Joined both dataframes to get a graph of episodes(count) and suicide no.


# In[40]:


df_join = jn.r_index(df_join)# Changing the index and creating the column "year"


# In[41]:


fig = jn.year_suic_season(df_join);
fig.figure.savefig("su_ep.jpg", dpi=1000)


# In[ ]:




