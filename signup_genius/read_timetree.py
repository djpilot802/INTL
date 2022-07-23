# %%
import requests 
import pandas as pd
import time 
import numpy as np

intl_url = 'https://www.signupgenius.com/go/10c0f4aaeab2fa2fac07-july'

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

r = requests.get(intl_url, headers=header)

# %%
dfs = pd.read_html(r.text)
df = dfs[3]
df.rename(columns={0:'Role', 2:'Person'} , inplace = True)
df.drop(columns=1, inplace = True)
df.head(20)

# %% [markdown]
# # Remove Slots and Signup from Person

# %%
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

df['Person'] = df['Person'].str.replace('|'.join(to_remove),"")
df['Person'] = df['Person'].str.replace('Joshua Reeves Reeves','Joshua Reeves')
df['Person'] = df['Person'].str.replace('Bill Collins Collins','Bill Collins')

# %% [markdown]
# # Split Role Column

# %%
df['Role'] = df['Role'].str.split('(').str[0]
df.head(50)

verb = []

for i in df['Role']: 
    if 'Greeter' in i:
        i = 'greet(s)!'
    elif 'Topic' in i: 
        i = 'brings topic!'
    elif 'Secretary' in i: 
        i = 'Secretarys!'
    verb.append(i)

df['Verb'] = verb
df.head(40)

# %%
df['First Person'] = df['Person'].str.split().str[0]
df['Second Person'] = df['Person'].str.split().str[2]
df['Third Person'] = df['Person'].str.split().str[4]
df = df.fillna('')
df.head(50)

# %%
df.to_csv(r'data.csv')


