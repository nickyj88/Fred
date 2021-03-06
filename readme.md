# FRED App
#### This Flask app collects and loads data from the FRED api's GDPCI, UMC Sentiment Index, and Unemployment rate series. 

## Building the app:
##### Clone the repository. You'll need virtualenv, which you can pip install. This app uses pip with Python 3.
```python 
pip install virtualenv
source venv/bin/activate
pip install requirements.txt
```

##### And you will have the environment set up. You will also need to have postgresql installed and supply the pg credentials to the fred.app file so that the application can run a postgres instance locally.

##### Using SQLAlchemy means I didn't have to use SQL to set up the DB (bless ORMs), but I have included a python script that would run the postgres commands to create the tables once you have the data collected from the FRED API and run a
```python
db.create_all()
```
##### in a python environment with the database object imported.

##### From there you can run the app:
```python
python app/fred.py
```
#### Load up localhost:5000 in browser.
###### Loading the home route will make a GET request, which queries the database and renders the average yearly unemployment rates from 1980-2015.

###### The update data button triggers the api calls and merges in new records discovered by the request to the FRED API. We can very easily set up a form to take a sql query and pass that through to return and render the results of a few stock queries we may want to run.

##### We can check out the data tables in psql 

###### Classes may be unnecessary at this point, but they allow for quick joining via foreign keys that would make any kind of interaction much smoother when we want to see different series in the same view or visualization.

### Avg Unemployment:
###### The app handles this when you load up localhost in browser, but the script unemployment.py will query the database and return an object to memory with the yearly average of unemployement rates in a pandas dataframe for any analysis we may want to do interactively. It probably makes sense to leave the data as is (rather than filtering and rolling up in SQL) so we can do more manipulation in pandas.

#### Automation:
###### We can use celery to automate the data updates: http://flask.pocoo.org/docs/0.10/patterns/celery/ 

#### Realtime_start:
###### This makes the possibilities much more interesting when we analyze this data because it is now a much richer dataset capable of answering questions about the how the instruments and methodologies we use to collect the data have evolved. There could be some interesting visualizations using these numerical states to show how misinformation may have driven policy decisions or market changes.
