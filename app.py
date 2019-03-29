from flask import Flask, render_template, request, redirect

# Qu xcpuajeyffeoNLoSEozx
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


