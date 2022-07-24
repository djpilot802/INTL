#!/usr/bin/env python
# coding: utf-8

# In[1]:


# %%
import requests 
import pandas as pd
import time 
import numpy as np
import re

print("Reading Timetree website and analyzing data...")

# Reading in Signup Genius URL and data

intl_url = 'https://www.signupgenius.com/go/10c0f4aaeab2fa2fac07-july'

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

r = requests.get(intl_url, headers=header)

# Finding the right table on the page

dfs = pd.read_html(r.text)
df = dfs[3]
df.rename(columns={0:'Role', 2:'Person'} , inplace = True)
df.drop(columns=1, inplace = True)

# %%
# Cleaning up data - removing double names, signup, slots filled, etc. 

to_remove = {
    '2 of 3 slots filled',
    'All slots filled',
    'Sign Up',
    'O yeah'
}

to_replace = {
    'Joshua Reeves Reeves' : 'Joshua Reeves',
    'Bill Collins Collins' : 'Bill Collins'
}

df['Person'] = df['Person'].str.replace('|'.join(to_remove),"", regex = True)
df['Person'] = df['Person'].str.replace('Joshua Reeves Reeves','Joshua Reeves')
df['Person'] = df['Person'].str.replace('Bill Collins Collins','Bill Collins')
df['Person'] = df['Person'].str.replace('Jesse J Gage','Jesse Gage')

df['Role'] = df['Role'].str.split('(').str[0]

# %%
# Adding emoji for data:attributes:title

emoji = []

#Emojis are below! 

# TOPIC GUITAR = U0001F3B8
# GREET BANJO = U0001FA95
# SECRETARY MICROPHONE = U0001F3A4

for i in df['Role']: 
    if 'Greeter' in i:
        i = "\U0001FA95 "
    elif 'Topic' in i: 
        i = "\U0001F3B8 " 
    elif 'Secretary' in i: 
        i = "\U0001F3A4 "
    emoji.append(i)

df['Emoji'] = emoji

# %%
# Adding verb for data:attributes:title

verb = []

for i in df['Role']: 
    if 'Greeter' in i:
        i = 'greet!'
    elif 'Topic' in i: 
        i = 'brings topic!'
    elif 'Secretary' in i: 
        i = 'Secretarys!'
    verb.append(i)

df['Verb'] = verb
df.head(40)

df['first'] = df['Person'].str.split().str[0]
df['second'] = df['Person'].str.split().str[2]
df['third'] = df['Person'].str.split().str[4]
df = df.fillna('')
df['Combined'] = df['first'] + " " + df['second'] + " " + df['third']
df['Count'] = df['Combined'].str.split().str.len()

df.loc[df['Count'] == 3, 'data:attributes:title'] = df['Emoji'] + df['first'] + ", " + df['second'] + " & " + df['third'] + " " + df['Verb']
df.loc[df['Count'] == 2, 'data:attributes:title'] = df['Emoji'] + df['first'] + " & " + df['second'] + " " + df['Verb']
df.loc[df['Count'] == 1, 'data:attributes:title'] = df['Emoji'] + df['first'] + " " +  df['Verb']

# %%
# Cleaning for export 

df['Day'] = df['Role'].str.split().str[0]
df['Role'] = df['Role'].str.split(" ", 1).str[1]
df.drop(columns={'Person','Verb','first','second','third','Combined','Count','Emoji'} , inplace = True)
df = df[['Day','Role','data:attributes:title']]
df.head()


# In[6]:


script_url = 'https://docs.google.com/document/d/1tVsWegpQ8LR7J20m8sRVA9z-XuKPzDwX7d8yQER-X1c/edit?usp=sharing'
zoom_url = 'https://us04web.zoom.us/j/406536344'
df.head()

url = []

for i in df['Role']: 
    if 'Greeter' in i:
        i = zoom_url
    elif 'Topic' in i: 
        i = zoom_url
    elif 'Secretary' in i: 
        i = script_url
    url.append(i)

df['url'] = url
df.head(40)

# %%
# Exporting File to .csv

print("Data exporting...")
df.to_csv(r'/Users/jaccottam/Desktop/Projects/INTL/db/timetree.csv')
print("Data exported to db Check for file named timetree.csv.")