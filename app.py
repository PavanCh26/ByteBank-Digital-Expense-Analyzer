from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)

# ---------- File Paths ----------
USERS_FILE = "users.json"
DATA_FILE = "data.json"


# ---------- Helper Functions ----------
def load_users():
    """Load users from JSON file"""
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump([{"username": "admin", "password": "1234"}], f)
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def load_data():
    """Load expense data from JSON file"""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    """Save expense data to JSON file"""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------- Routes ----------
@app.route("/")
def login_page():
    return render_template("login.html", message="")


@app.route("/login", methods=["POST"])
def login():
    """Validate login credentials"""
    username = request.form["username"]
    password = request.form["password"]
    users = load_users()

    for user in users:
        if user["username"] == username and user["password"] == password:
            return redirect(url_for("dashboard"))
    return render_template("login.html", message="Invalid username or password!")


@app.route("/dashboard")
def dashboard():
    """Main dashboard showing all expenses and summary"""
    data = load_data()
    total = sum(item["amount"] for item in data) if data else 0
    highest = max((item["amount"] for item in data), default=0)
    lowest = min((item["amount"] for item in data), default=0)
    return render_template(
        "dashboard.html",
        expenses=data,
        total=total,
        highest=highest,
        lowest=lowest
    )


@app.route("/add", methods=["POST"])
def add_expense():
    """Add new expense"""
    name = request.form["name"]
    amount = float(request.form["amount"])
    category = request.form["category"]

    data = load_data()
    data.append({"name": name, "amount": amount, "category": category})
    save_data(data)
    return redirect(url_for("dashboard"))


@app.route("/delete/<int:index>")
def delete_expense(index):
    """Delete an expense by index"""
    data = load_data()
    if 0 <= index < len(data):
        data.pop(index)
        save_data(data)
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
                       
