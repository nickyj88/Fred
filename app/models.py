from flask.ext.sqlalchemy import SQLAlchemy
from fred import app

db = SQLAlchemy(app)
 
 
 
class Gdpc1 (db.Model):
  __tablename__ = "gdp_totals"
  observation_date = db.Column('observation_date', db.Date, primary_key=True) 
  gdp_value = db.Column('gdp_value_millions', db.Float)
 
 
class UMConsumerSentimentIndex (db.Model):
  __tablename__ = "consumer_sentiment_indexes"
  observation_date = db.Column('observation_date', db.Date, primary_key=True) 
  sentiment_index = db.Column('sentiment_index', db.Float)

 
class UnemploymentRate (db.Model):
  __tablename__ = "unemployment_rates"
  observation_date = db.Column('observation_date', db.Date, primary_key=True) 
  unemployment_rate = db.Column('unemployment_rate', db.Float)