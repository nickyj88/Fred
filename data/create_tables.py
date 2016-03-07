import psycopg2 as pg
import pandas as pd

conn_string = "host='localhost:5000' \
                dbname='fred' user='nickjames' password='monkeys' port='5439'"

conn = pg.connect(conn_string)

cur = conn.cursor()

data_object = {}

def interpolate_insert_values(row_list):
  value_string = ''
  for row in row_list:
    value_string = value_string + "(" + row[0] + ", " + row[1] + ")"


def create_and_insert(data_object):
  create_strings = []
  insert_strings = []

  for table in data_object.keys():
    create_strings.append("CREATE TABLE {} (observation_date TIMESTAMP, value REAL);".format(table))

  for table, values in data_object.items():
    insert_string = "INSERT INTO {0} VALUES ({1})".format(table, interpolate_insert_values(values))
    insert_string = insert_string + ";"
    insert_strings.append(insert_string)

    cur.executemany(create_strings)
    conn.commit()

    cur.executemany(insert_strings)
    conn.commit()
    conn.close()



