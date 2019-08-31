import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""


    stocks = db.execute("SELECT stock, shares, price FROM purchases WHERE id = :id", id = session['user_id'])

    result = db.execute("SELECT cash FROM users WHERE id = :id", id = session['user_id'])

    total_cash = float(result[0]['cash'])

    grand_total = total_cash

    for stock in stocks:
        symbol = stock["stock"]
        print(symbol)
        shares = stock["shares"]
        print("share", shares)
        quote = lookup(symbol)
        print(quote)
        price = float(quote["price"])
        print("price", price)
        total = float(price * shares)
    grand_total += total

    return render_template("index.html", stocks = stocks, cash = total_cash, grand_total = grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":

        # Render an apology if the input is blank or does not exist
        quote = lookup(request.form.get("symbol"))

        if request.form.get("symbol") == "":
            return apology("Please Enter in a stock", 403)

        elif quote == None:
            return apology("Stock does not exist", 403)
        print(quote)

        # call lookup to look up a stock’s current price.
        price = quote["price"]
        print("Price:", price)

        # Get current user's cash
        funds = db.execute("SELECT cash FROM users WHERE id = :id", id = session["user_id"])
        print(funds[0]["cash"])

        shareInput = int(request.form.get("shares"))
        print(shareInput)

        # Require that a user input a number of shares, Render an apology if the input is not a positive integer.
        if shareInput < 1:
            return apology("Please input a positive number of shares", 403)

        if funds[0]["cash"] < price * shareInput:
            return apology("Sorry you have insufficient funds for this purchase", 403)

        print(funds[0]["cash"] - (price * shareInput))

        # update purchases history
        db.execute("INSERT INTO purchases (id, stock, shares, price) VALUES (:id, :stock, :shares, :price)",
            id = session["user_id"],
            stock = quote["symbol"],
            shares = shareInput,
            price = usd(quote["price"]))

        # update users cash
        db.execute("UPDATE users SET cash = cash - :purchase WHERE id = :id",
            id = session["user_id"],
            purchase = shareInput * price)


    return render_template("buy.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    return jsonify("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # print(rows)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        print(rows[0]["id"])

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        quote = lookup(request.form.get("symbol")) # quote = {'name': 'Netflix, Inc.', 'price': 289.2, 'symbol': 'NFLX'}
        print(quote)
        # print(quote["name"]) = Netflix, Inc.
        # print(quote["price"]) = 289.2
        # print(quote["symbol"]) = NFLX

        if quote == None:
            return apology("Stock does not exist", 403)

        name = quote["name"]
        price = quote["price"]
        symbol = quote["symbol"]

        return render_template("quoted.html", name=name, price=price, symbol=symbol)

    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Render an apology if the user’s input is blank
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide password confirmation", 403)

        # Check if passwords match
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if password != confirmation:
            return apology("passwords do not match", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                      username=request.form.get("username"))

        # Check if username already exists
        if len(rows) == 1:
            return apology("Username already exists", 403)

        username = request.form.get("username")

        hash = generate_password_hash(password)
        # print(username)
        # print(hash)

        db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=username, hash=hash)
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                      username=request.form.get("username"))
        print(rows)

        # Remember which user has registered
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
