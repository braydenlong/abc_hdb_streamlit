import requests
import pandas as pd
import json
from langchain_community.document_loaders import PyMuPDFLoader

# datasetId = "d_8b84c4ee58e3cfc0ece0d773c8ca6abc"
# url = "https://data.gov.sg/api/action/datastore_search?"

# filters = {
#     "month": ['2023-01', '2023-02', '2023-03', '2023-04', '2023-05', 
#               '2023-06', '2023-07', '2023-08', '2023-09', '2023-10', '2023-11', '2023-12']
# }
# params = {
#     'resource_id': datasetId,
#     'limit': 1000,
#     'sort': 'resale_price asc',
#     'filters': json.dumps(filters)
# }
# response = requests.get(url, params=params)
# data = response.json()
# print(data)
# records = data.get('result', {}).get('records', [])
# df = pd.DataFrame(records)
# print(df)

filepath = "https://www.hdb.gov.sg/-/media/doc/EAPG-CSC/Resale-Terms--Conditions-9-May-2023-updated.pdf"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Make a request to download the PDF
response = requests.get(filepath, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    with open('document.pdf', 'wb') as f:
        f.write(response.content)

    # Load the document using PyMuPDFLoader
    loader = PyMuPDFLoader('document.pdf')
    documents = loader.load()
    print('success')
else:
    print(f"Failed to download the document, status code: {response.status_code}")