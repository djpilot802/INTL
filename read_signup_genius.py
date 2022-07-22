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

dfs = pd.read_html(r.text)
df = dfs[3]
df.drop(columns = 1, inplace = True)
df.rename(columns = {0:'Role', 2: 'Person'} , inplace = True)

print(df.head(15))

