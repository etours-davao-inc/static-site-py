from flask import Flask, render_template

import json
from datetime import datetime

import config

app = Flask(__name__)

with open(config.dataSource) as dataSource:
  tourpackages = json.load(dataSource)

with open(config.dataSource2) as indexData:
  indexData = json.load(indexData)

tp = {}
for tourpackage in tourpackages:
  tp[tourpackage['slug']] = tourpackage

sortedTourpackages = sorted(tourpackages, key=lambda k: k['total_hours']) 

@app.route('/')
def index():
  return render_template('index.html', tourpackages=sortedTourpackages, indexData=indexData)

@app.route('/philippine-tours-2019-2020/davao-tourpackages/<slug>')
def tourpackage_page(slug):
  tourpackage = tp[slug]
  today = datetime.now().strftime('%m/%d/%Y')
  return render_template('tourpackage.html', tourpackage=tourpackage, today=today)

@app.route('/davao-tours-2019-2020')
def tourpackages():
  found = len(sortedTourpackages)
  return render_template('tourpackages.html', tourpackages=sortedTourpackages, found=found)

@app.route('/company-profile')
def companyprofile():
  return render_template('company-profile.html')

@app.route('/contact-us')
def contactus():
  return render_template('contact-us.html')

@app.route('/privacy-policy')
def privacypolicy():
  return render_template('privacy-policy.html')  

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html') 

if __name__ == '__main__':
  app.run(debug=True)