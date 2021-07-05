from bokeh.plotting import figure
# from bokeh.io import output_file,show
import pandas
from bokeh.plotting import figure, output_file, show

df = pandas.read_excel("verlegenhuken.xlsx",sheet_name=0)

x = df["Temperature"] /10
y = df["Pressure"] /10

p = figure(plot_width=500, plot_height=400, tools='pan')

p.title.text = "Temperature and Air Pressure"
p.title.text_color = "Gray"
p.title.text_font = "times"
p.title.text_font_style = "bold"
p.xaxis.minor_tick_line_color = "Yellow"
p.yaxis.minor_tick_line_color = "Blue"
p.xaxis.axis_label = "Temperature( c)"
p.yaxis.axis_label = "Pressure ( InPa)"

p.circle(x, y, size=0.5)
#p.circle(df["Temperature"],df["Pressure"],size=0.5)
output_file("graph.html")
show(p)

# df=pandas.read_excel("verlegenhuken.xlsx")
# df=pandas.read_csv("http://pythonhow.com/data/bachelors.csv")
# df=pandas.read_csv("http://pythonhow.com/data/verlegenhuken.xlsx")
