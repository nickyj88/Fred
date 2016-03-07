from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

from views import *

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nickjames:monkeys@localhost/fred'

if __name__ == "__main__":
  app.run(debug=True)