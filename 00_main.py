import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from google.auth.transport import requests


credentials = service_account.Credentials.from_service_account_file('service_account.json')

project_id = 'abc'

client = bigquery.Client(credentials= credentials,project=project_id)


query_job = client.query("""
  SELECT *
  FROM tabename
  LIMIT 10""")
results = query_job.result()

for row in results:
        print(row)