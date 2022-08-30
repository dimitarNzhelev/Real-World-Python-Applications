from motion_detect import df
from bokeh.io import curdoc
from bokeh.plotting import figure, show, output_file
from bokeh.models import Range1d

p = figure(x_axis_type = 'datetime', height = 300, width = 500, sizing_mode = "", title = "Motion Graph")
curdoc().theme = 'dark_minimal'
p.y_range = Range1d(0,1)
q = p.quad(left=df["Start"], right=df["End"], bottom=0, top=1, color="green")

output_file("Motion.html")
show(p)
