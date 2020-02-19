from flask import Flask, render_template

from util import chart1, chart2

# ---- Flask setup. - ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', chart1=chart1.chart(), chart2=chart2.chart())

@app.errorhandler(404)
def not_found_error(error):
    return render_template('/error/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('/error/500.html'), 500
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----




