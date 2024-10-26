import requests
import pandas as pd
import json

datasetId = "d_8b84c4ee58e3cfc0ece0d773c8ca6abc"
url = "https://data.gov.sg/api/action/datastore_search?"

filters = {
    "month": ['2023-01', '2023-02', '2023-03', '2023-04', '2023-05', 
              '2023-06', '2023-07', '2023-08', '2023-09', '2023-10', '2023-11', '2023-12']
}
params = {
    'resource_id': datasetId,
    'limit': 1000,
    'sort': 'resale_price asc',
    'filters': json.dumps(filters)
}
response = requests.get(url, params=params)
data = response.json()
print(data)
records = data.get('result', {}).get('records', [])
df = pd.DataFrame(records)
print(df)