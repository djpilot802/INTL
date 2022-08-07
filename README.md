# INTL

# Welcome to the INTL App 

This app helps to automate and speed-up actions associated with the INTL group. Happy that you're joing. It's currently a work in progress and I'm making daily updated until a complete and viable first product is finished. 

This is currently in an **alpha** pre-release phase and is being updated regulary. 

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
python participant_zoom.py
```
Alternatively, you could just execute the below: 
```bash 
python Desktop/Projects/intl/zoom/participant_zoom.py
```

4. This will launch the meeting if you're logged in, and open the INTL script and daily reflection. 

## Logging into the Meeting

You can use the username: 

```
itsnottoolate1030@gmail.com
```

You can use the below password: 

```
itsnotTOOlate8
```

Pasting into Timetree: 

```
It’s Not Too Late’s 7th tradition virtual basket - Cash App - $1030INTL

Service Work Signup: https://bit.ly/3v9aFO7

INTL Anonymous Ask-It Basket: https://t8qg8dvqojx.typeform.com/to/rnNg3xav
```
## To Do: 

- [x] Read Signup genius and convert to frame 
- [x] Remove unnecessary values and text errors like signup and slots added 
- [x] Split names into three individuals 
- [x] Started oauth process, but it keeps re-directing endlessly
- [x] Obtain an access token
- [x] Complete OAuth App
- [x] Read members json data into df
- [x] Read events from jason data into df
- [x] Complete date and day functions 
- [ ] Write completed dataframe to Timetree - this is going to take a very long time and be complicated
- [ ] Improve and automate
- [ ] Determine the right path forward for new releases