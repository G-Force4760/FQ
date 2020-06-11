import pandas as pd 
from bokeh.plotting import figure
from bokeh.io import show, output_file
from bokeh.models import Span, Range1d, ColumnDataSource, LabelSet

output_file('N:\CODING\Python\Projetos\FQ\Rua\eletrico\poste eletrico.html')

df = pd.read_csv('N:\CODING\Python\Projetos\FQ\Rua\eletrico\poste eletrico.csv')

aparelhos = ['Campo elétrico (V/m)', 'Campo magnético (nT)']

campo = [float(df['Campo elétrico (V/m)']), float(df['Campo magnético (nT)'])]



f = figure(plot_height=300, x_range=aparelhos, title='Casa de banho - Campo elétrico', toolbar_location='above')
f.vbar(x=aparelhos, top=campo, width=0.9)

source = ColumnDataSource(dict(x=aparelhos,y=campo))
labels = LabelSet(x='x', y='y', text='y', level='glyph', x_offset=-13.5, y_offset=0, source=source, render_mode='canvas')
f.add_layout(labels)

f.y_range = Range1d(0, 270, bounds=(0, None))
f.yaxis.visible = False
f.xaxis.axis_label = 'Poste de 60 kV'
f.xgrid.grid_line_color = None
f.y_range.start = 0


show(f)