from fred import app
from flask import render_template, request, url_for
from models import db, Gdpc1, UMConsumerSentimentIndex, UnemploymentRate
import requests
 
@app.route('/', methods=["GET", "POST"])
def index():

# Returns a list with a dictionary object for each series passed in the args.
# This function takes 3 parameters: 
#   1) A list of strings that will be passed into the URL.
#   2) An API Key (generated at research.stlouisfed.org)
#   3) A base url to direct the query
  def collect_data(series, key, url1):
    # Collect the data
    url2 = "&api_key="
    url3 = "&file_type=json"
    data = {}

    for i in series:
      url = url1 + i + url2 + key + url3
      r = requests.get(url)
      data[i] = r.json()

    # Prepare the data for loading

    flattened_data = {}
    for table_name, data_set in data.items():
      mylist = [[observation["date"], observation["value"]] for observation in data_set["observations"]]
      flattened_data[table_name] = mylist

    return flattened_data
 
  # Loads new collected data into postgres database.
  # Takes no args; api params are hard coded and passed to collect_data function.
  def load_data():  
    url1 = "https://api.stlouisfed.org/fred/series/observations?series_id="
    key = "19dede202896425a8700c0682a1b3b16"
    series = ["GDPC1", "UMCSENT", "UNRATE"]
    
    collected_data = collect_data(series, key, url1)
    
    session = db.session()

    for row in collected_data["GDPC1"]:
      date = row[0]
      value = float(row[1]) if row[1] != '.' else None
      d = Gdpc1(observation_date=date, gdp_value=value)
      session.merge(d)

    for row in collected_data["UMCSENT"]:
      date = row[0]
      value = float(row[1]) if row[1] != '.' else None      
      d = UMConsumerSentimentIndex(observation_date=date, sentiment_index=value)
      session.merge(d)


    for row in collected_data["UNRATE"]:
      date = row[0]
      value = float(row[1]) if row[1] != '.' else None      
      d = UnemploymentRate(observation_date=date, unemployment_rate=value)
      session.merge(d)

    session.commit()

  query = """
  SELECT
    date_trunc('year', observation_date) AS year,
    AVG(unemployment_rate) avg_unemployment_rate
  FROM unemployment_rates
  WHERE observation_date BETWEEN '1980-01-01' AND '2015-12-31'  
  GROUP BY 1
  ORDER BY 1 DESC;
  """

  unemployment_rates = db.engine.execute(query).fetchall()

  if request.method == "POST":
    load_data()

  return render_template('index.html', unemployment_rates=unemployment_rates)





