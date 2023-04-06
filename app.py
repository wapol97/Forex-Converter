from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates

app = Flask(__name__)

app.config['SECRET_KEY'] = "1234567890"
debug = DebugToolbarExtension(app)