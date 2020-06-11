from bokeh.plotting import figure
from bokeh.io import show, output_file
from bokeh.models import Range1d, ColumnDataSource, LabelSet
from scipy.interpolate import interp1d
import numpy as np

output_file('N:\CODING\Python\Projetos\FQ\Casa\sala de estar\carregador do computador\eletrico\carregador eletrico.html')



d = [0.000, 0.015, 0.030, 0.045]

e = [78.13, 14.67, 8.847, 6.256]

g = interp1d(d, e, kind='quadratic')
d2 = np.linspace(0, 0.045, 1000)
e2 = g(d2)

f = figure(plot_height=300, title='Carregador do computador - Campo elétrico', toolbar_location='above')

source = ColumnDataSource(dict(x=d, y=e))
labels = LabelSet(x='x', y='y', text='y', level='glyph', x_offset=10, y_offset=5, source=source, render_mode='canvas')
f.add_layout(labels)

f.x_range = Range1d(0, 0.06, bounds=(0, None))
f.y_range = Range1d(0, 100, bounds=(0, None))
f.xaxis.axis_label = 'd (m)'
f.yaxis.axis_label = 'E (V/m)'
f.xgrid.grid_line_color = None
f.y_range.start = 0
f.line(d2, e2, line_width=2, legend_label='Variação do campo elétrico')
f.circle(d, e, fill_color="green", size=8)

show(f)