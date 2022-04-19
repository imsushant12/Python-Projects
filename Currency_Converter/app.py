from flask import Flask, render_template, request
import requests

# Initializing Flask app.
app = Flask(__name__)


# A function to extract api key from the credentials.txt file.
def get_api_key():
    with open("credentials.txt") as f:
        API = f.readline()
        return API


# A function to calculate the exchange rates b/w teo currencies.
def exchange_rate(currency1, currency2):
    endpoint = (
        f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    )
    url = BASE_URL + endpoint
    data = requests.get(url).json()

    if len(data) == 0:
        return

    rate = list(data.values())[0]

    return rate


# A function to convert the amount in first currency to second.
def convert(currency1, currency2, amount):
    # getting the exchange rate.
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        return

    converted_amount = rate * amount
    return converted_amount


# Setting the complete url for accessing the api data.
BASE_URL = "https://free.currconv.com/"
API_KEY = get_api_key()


# Function to get currencies as a list.
def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = requests.get(url).json()["results"]

    data = list(data.items())
    data.sort()
    currencies = []
    for name, currency in data:
        name = currency["currencyName"]
        _id = currency["id"]
        symbol = currency.get("currencySymbol", "---")
        currencies.append([name, _id, symbol])

    return currencies


# setting the route(s).
@app.route("/home", methods=["POST", "GET"])
@app.route("/", methods=["POST", "GET"])
def home():
    currencies = get_currencies()
    if request.method == "POST":
        first_currency = request.form.get("first_currency")
        second_currency = request.form.get("second_currency")
        amount = request.form.get("amount")

        result = convert(first_currency, second_currency, amount)

        return render_template("home.html", info = currencies, result = result)
    return render_template("home.html", info = currencies, result = 0)


if __name__ == "__main__":
    app.run(debug=True)

    