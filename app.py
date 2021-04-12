from flask import Flask, render_template
from model_files.main import getTrends, getSentiments
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    tlist = getTrends()
    sts = getSentiments()
    return render_template('index.html', trends=tlist, sentiments=sts)

if __name__=='__main__':
    app.run(debug=True)
