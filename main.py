import pandas as pd
import plotly.express as px


def readAndPlot(fileName, xValue, yValue, colorValue):
    df = pd.read_csv(fileName)
    fig = px.scatter(df, x=xValue, y=yValue, color=colorValue)
    fig.show()


fileName = input('fileName : ')
x = input('x : ')
y = input('y : ')
color = input('color : ')

readAndPlot(fileName, x, y, color)
