# Returns a dataframe with the average unemployment rates grouped by year
# Could be more malleable if we leave the grouping to pandas
# But this is a very specific question.
def average_unemployment_rate():
  query = """
  SELECT
    date_trunc('year', observation_date),
    AVG(value) avg_yearly_unemployment_rate
  FROM unemployment_rates
  WHERE observation_date BETWEEN '1980-01-01' AND '2015-12-31'  
  GROUP BY 1
  """
  df = pd.read_sql(query, conn)
  return df