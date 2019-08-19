from flask import Flask, render_template

import json
from datetime import datetime

import config

app = Flask(__name__)

with open(config.dataSource) as dataSource:
  tourpackages = json.load(dataSource)

tp = {}
for tourpackage in tourpackages:
  tp[tourpackage['slug']] = tourpackage

@app.route('/')
def index():
  sortedTourpackages = sorted(tourpackages, key=lambda k: k['total_hours'])  
  return render_template('index.html', tourpackages=sortedTourpackages)

@app.route('/philippine-tours-2019-2020/davao-tourpackages/<slug>')
def tourpackage(slug):
  tourpackage = tp[slug]
  today = datetime.now().strftime('%m/%d/%Y')
  return render_template('tourpackage.html', tourpackage=tourpackage, today=today)

if __name__ == '__main__':
  app.run(debug=True)