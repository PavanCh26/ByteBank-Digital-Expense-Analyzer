from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def dashboard():
    data = load_data()
    total = sum(item["amount"] for item in data) if data else 0
    highest = max((item["amount"] for item in data), default=0)
    lowest = min((item["amount"] for item in data), default=0)
    return render_template("dashboard.html", expenses=data, total=total, highest=highest, lowest=lowest)

@app.route("/add", methods=["POST"])
def add_expense():
    name = request.form["name"]
    amount = float(request.form["amount"])
    category = request.form["category"]
    data = load_data()
    data.append({"name": name, "amount": amount, "category": category})
    save_data(data)
    return redirect(url_for("dashboard"))

@app.route("/delete/<int:index>")
def delete_expense(index):
    data = load_data()
    if 0 <= index < len(data):
        data.pop(index)
        save_data(data)
    return redirect(url_for("dashboard")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
