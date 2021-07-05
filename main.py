from bokeh.plotting import figure
#from bokeh.io import output_file,show
import pandas
from bokeh.plotting import figure, output_file, show



df=pandas.read_excel("verlegenhuken.xlsx")
#df=pandas.read_csv("http://pythonhow.com/data/bachelors.csv")
#df=pandas.read_csv("http://pythonhow.com/data/verlegenhuken.xlsx")
x=df["Temperature"]
y=df["Pressure"]

output_file("Line_temperature.html")

f =figure()

#f.triangle(x,y)
f.circle(x,y)

show(f)