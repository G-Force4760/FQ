import pandas as pd 
from bokeh.plotting import figure
from bokeh.io import show, output_file
from bokeh.models import Span, Range1d, ColumnDataSource, LabelSet

output_file('N:\CODING\Python\Projetos\FQ\Casa\cozinha\magnético\cozinha magnetico.html')

df = pd.read_csv('N:\CODING\Python\Projetos\FQ\Casa\cozinha\magnético\cozinha magnetico.csv')

aparelhos = ['torradeira','cafeteira','varinha mágica','robot de cozinha','jarro elétrico']

campo = [float(df['torradeira']), float(df['cafeteira']), float(df['varinha mágica']), float(df['robot de cozinha']), float(df['jarro elétrico'])]



f = figure(plot_height=300, x_range=aparelhos, title='Cozinha - Campo magnético', toolbar_location='above')
f.vbar(x=aparelhos, top=campo, width=0.9)

source = ColumnDataSource(dict(x=aparelhos,y=[2.069,30.06,3.754,22.45,6.521]))
labels = LabelSet(x='x', y='y', text='y', level='glyph', x_offset=-13.5, y_offset=0, source=source, render_mode='canvas')
f.add_layout(labels)

f.y_range = Range1d(0, 210, bounds=(0, None))
span = Span(location=200, dimension='width', line_color='red', line_dash='dashed', line_width=1)
f.xaxis.axis_label = 'Aparelhos'
f.yaxis.axis_label = 'B (uT)'
f.xgrid.grid_line_color = None
f.y_range.start = 0
f.add_layout(span)

show(f)