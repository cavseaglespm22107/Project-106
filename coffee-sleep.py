import plotly.express as px
import csv
import numpy as np
def getDataSource(dataPath):
    icecreamsales = []
    colddrinksales = []
    with open(dataPath) as f:
        df = csv.DictReader(f)
        for i in df:
            icecreamsales.append(float(i["Coffee in ml"]))
            colddrinksales.append(float(i["sleep in hours"]))
    return {"x": icecreamsales, "y": colddrinksales}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between ", correlation[0,1])
def setup():
    dataPath = "coffee_sleep.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

setup()