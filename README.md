# INTL

# Welcome to the INTL App 

This app helps to automate and speed-up actions associated with the INTL group. Happy that you're joing. It's currently a work in progress and I'm making daily updated until a complete and viable first product is finished. 

## Installing Python on your Machine

- Navigate to https://www.python.org/downloads/
- Install the appropriate python bundle for your machine!
- In the command prompt ensure you have the required libraries: 

 ```bash
$ pip install -r requirements.txt
```

## Use 

### Automating Zoom Login 

1. Ensure that you're logged into Zoom on your webbrowser. 
2. Select the zoom folder or in the cmd cd/Desktop/Projects/intl/zoom
3. Run the python file! cmd python zoom_login.py

```bash 
$ python zoom_login.py
```

4. This will launch the meeting if you're logged in, and open the INTL script and daily reflection. 

## To Do: 

- [x] Read Signup genius and convert to frame 
- [x] Remove unnecessary values and text errors like signup and slots added 
- [x] Split names into three individuals 
- [x] Started oauth process, but it keeps re-directing endlessly
- [x] Obtain an access token
- [ ] Complete OAuth App
- [ ] Complete date and day functions 
- [ ] Write completed dataframe to Timetree 
- [ ] Improve and automate
- [ ] Determine the right path forward for new releases