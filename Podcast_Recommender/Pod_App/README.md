### Podcast Web App

Code for podcast recommender web app.

**Components**
1. `main.py` - This is the main Python code that uses Flask and calls py_podcasts.py to use the model
2. `py_podcasts.py` - This is a separate Python script that reads in the pickled model and also preps the data for the model
3. `pod_df.gz` - The pickled/zipped matrix of podcast similarities 
4. `index.html` not included in this repo, but it is the webpage that will take inputs for the model and output a result on the webpage
