from flask import Flask, render_template

import json
from datetime import datetime
from flask_static_compress import FlaskStaticCompress
from flask_htmlmin import HTMLMIN

import config

app = Flask(__name__)
app.config['MINIFY_PAGE'] = True
app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html'
compress = FlaskStaticCompress(app)

htmlmin = HTMLMIN(app)

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

@app.route('/tourpackage/<slug>.html')
def tourpackage_page(slug):
  tourpackage = tp[slug]
  today = datetime.now().strftime('%m/%d/%Y')
  return render_template('tourpackage.html', tourpackage=tourpackage, today=today, data=json.dumps(tourpackage))

@app.route('/tourpackages.html')
def tourpackages():
  found = len(sortedTourpackages)
  return render_template('tourpackages.html', tourpackages=sortedTourpackages, found=found)

@app.route('/company-profile.html')
def companyprofile():
  return render_template('company-profile.html')

@app.route('/contact-us.html')
def contactus():
  return render_template('contact-us.html')

@app.route('/privacy-policy.html')
def privacypolicy():
  return render_template('privacy-policy.html')

@app.route('/corporate-travel.html')
def corporateTravel():
  return render_template('corporate-travel.html')

@app.route('/404')
def page_not_found():
  return render_template('404.html') 

if __name__ == '__main__':
  app.run(debug=True)