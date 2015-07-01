import csv


def read_data(data):
    with open(data, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
        print data
    return data

data = 'County_Center_Populations.csv'
read_data(data)
