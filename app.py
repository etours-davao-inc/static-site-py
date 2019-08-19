from flask import Flask, render_template

import json

import config

app = Flask(__name__)

with open(config.dataSource) as dataSource:
  tourpackages = json.load(dataSource)

@app.route('/')
def index():
  sortedTourpackages = sorted(tourpackages, key=lambda k: k['total_hours'])  
  return render_template('index.html', tourpackages=sortedTourpackages)

@app.route('/philippine-tours-2019-2020/davao-tourpackages/<slug>')
def tourpackage(slug):
  return slug

if __name__ == '__main__':
  app.run(debug=True)