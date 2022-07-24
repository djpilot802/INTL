import webbrowser
import numpy as np

# Open zoom and make sure that it's running 
# LOG IN in your webbrowser - this will prevent you from logging out

# Open the meeting

print('Make sure you are logged into the host account!\t')
print('Just one second and Ill pull up the meeting, script, and daily reflection for you!')

url_zoom = 'https://us04web.zoom.us/j/406536344'
webbrowser.open(url_zoom , new = 2)

# Open the script and daily reflection

url_drive = 'https://docs.google.com/document/d/1tVsWegpQ8LR7J20m8sRVA9z-XuKPzDwX7d8yQER-X1c/view'
url_dr  = 'https://www.aa.org/pages/en_US/daily-reflection'

webbrowser.open(url_drive, new = 2)
webbrowser.open(url_dr, new = 2)
