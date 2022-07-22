import webbrowser

# Open zoom and make sure that it's running 
# LOG IN in your webbrowser - this will prevent you from logging out

# Open the meeting

url_zoom = 'https://us04web.zoom.us/j/406536344'
webbrowser.open(url_zoom , new = 0)

# Open the script and daily reflection

url_drive = 'https://docs.google.com/document/d/1tVsWegpQ8LR7J20m8sRVA9z-XuKPzDwX7d8yQER-X1c/view'
url_dr  = 'https://www.aa.org/pages/en_US/daily-reflection'

webbrowser.open(url_drive, new = 0)
webbrowser.open(url_dr, new = 0)
