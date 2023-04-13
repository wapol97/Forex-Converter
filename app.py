from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates


app = Flask(__name__)

app.config['SECRET_KEY'] = "1234567890"
debug = DebugToolbarExtension(app)


@app.route("/currency-exchange", methods=["GET"])
def currency_exchange():
    return render_template('base.html')

@app.route("/currency-exchange", methods=["POST"])
def exchange_result():
    currency = CurrencyRates()
    from_curr = request.form["from_curr"]
    to_curr = request.form["to_curr"]
    amount = request.form["amount"]

    msg = currency.convert(from_curr, to_curr, amount)
    
    flash(f"Your result is: {msg}", "result")

    return redirect('/currency-exchange')


if __name__=="__main__":
    app.run(debug=True)