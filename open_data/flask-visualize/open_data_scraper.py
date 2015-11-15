import csv

import requests

URL = "https://opendata.go.ke/api/views/i5bp-z9aq/rows.csv?accessType=DOWNLOAD"

def get_data():
    response = requests.get(URL)
    data = response.text
    results = {'children': []}
    for line in csv.DictReader(data.splitlines(), skipinitialspace=True):
        results['children'].append({
            'district': line['District Name'],
            'poverty_rate': line['Poverty Rate (2005-06)'],
            'number_of_poor_people': line['Number of Poor (2005-06)']
        })
    return results
