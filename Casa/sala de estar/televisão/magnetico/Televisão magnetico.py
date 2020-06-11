from bokeh.plotting import figure
from bokeh.io import show, output_file
from bokeh.models import Range1d, ColumnDataSource, LabelSet
from scipy.interpolate import interp1d
import numpy as np


output_file('N:\CODING\Python\Projetos\FQ\Casa\sala de estar\Televisão\magnetico\Televisão magnetico.html')



d = [0.000, 0.050, 0.100, 0.150, 0.200]

b = [284.4, 140.9, 61.28, 42.62, 23.02]
g = interp1d(d, b, kind='quadratic')
d2 = np.linspace(0, 0.2, 1000)
b2 = g(d2)

f = figure(plot_height=300, title='Televisão - Campo magnético', toolbar_location='above')

source = ColumnDataSource(dict(x=d, y=b))
labels = LabelSet(x='x', y='y', text='y', level='glyph', x_offset=10, y_offset=5, source=source, render_mode='canvas')
f.add_layout(labels)

f.x_range = Range1d(0, 0.3, bounds=(0, None))
f.y_range = Range1d(0, 320, bounds=(0, None))
f.xaxis.axis_label = 'd (m)'
f.yaxis.axis_label = 'B (nT)'
f.xgrid.grid_line_color = None
f.y_range.start = 0
f.line(d2, b2, line_width=2, legend_label='Variação do campo magnético')
f.circle(d, b, fill_color="green", size=8)

show(f)