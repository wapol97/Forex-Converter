from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = "1234567890"
debug = DebugToolbarExtension(app)

currency = CurrencyRates()

@app.route("/currency-exchange")
def currency_exchange():
    from_curr = request.form['from_curr']
    to_curr = request.form['to_curr']
    amount = request.form['amount']

    result = currency.convert(from_curr, to_curr, amount)
    
    return render_template('base.html', result)

    