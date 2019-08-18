from flask import Flask, render_template

import json

import config

app = Flask(__name__)

with open(config.dataSource) as dataSource:
  tourpackages = json.load(dataSource)

@app.route('/')
def index():
  for tourpackage in tourpackages:
    print(tourpackage['name'])
  return render_template('index.html', tourpackages=tourpackages)

if __name__ == '__main__':
  app.run(debug=True)