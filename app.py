from flask import Flask, render_template, request, redirect
import requests as re
import bs4
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import simplejson as json

from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, RangeTool
from bokeh.plotting import figure


# xcpuajeyffeoNLoSEozx
# 
# 
# GET https://www.quandl.com/api/v3/datasets/{database_code}/{dataset_code}/data.{return_format}
# curl "https://www.quandl.com/api/v3/datasets/WIKI/FB/data.json?api_key=xcpuajeyffeoNLoSEozx"


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/proc_symbol', methods=['POST'])
def hello():
    user_symbol = request.form['user_symbol']
    return user_symbol

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)

#user_symbol = 'FB'
geturl = 'https://www.quandl.com/api/v3/datasets/WIKI/'+user_symbol+'/data.json?api_key=xcpuajeyffeoNLoSEozx'
r = re.get(geturl)
json_data = json.loads(r.content.decode('utf-8'))['dataset_data']
df = pd.DataFrame(data=json_data['data'],columns=json_data['column_names'])

dates = np.array(df['Date'][::-1],dtype='datetime64')
close = np.array(df['Close'][::-1])

source = ColumnDataSource(data=dict(date=dates, close=close))


p = figure(plot_height=300, plot_width=800, tools="", toolbar_location=None,
           x_axis_type="datetime", x_axis_location="above",
           background_fill_color="#efefef", x_range=(dates[0], dates[1000]))

p.line('date', 'close', source=source)
p.yaxis.axis_label = 'Price'

select = figure(title="Drag the middle and edges of the selection box to change the range above",
                plot_height=130, plot_width=800, y_range=p.y_range,
                x_axis_type="datetime", y_axis_type=None,
                tools="", toolbar_location=None, background_fill_color="#efefef")

range_tool = RangeTool(x_range=p.x_range)
range_tool.overlay.fill_color = "navy"
range_tool.overlay.fill_alpha = 0.2

select.line('date', 'close', source=source)
select.ygrid.grid_line_color = None
select.add_tools(range_tool)
select.toolbar.active_multi = range_tool

show(column(p, select))

