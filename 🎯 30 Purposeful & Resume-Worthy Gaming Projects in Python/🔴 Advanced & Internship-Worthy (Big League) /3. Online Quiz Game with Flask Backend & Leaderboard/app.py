# app.py
from flask import Flask, jsonify, request, render_template, redirect, url_for
app = Flask(__name__)

QUESTIONS = [
    {"id":1,"q":"Capital of India?","options":["Delhi","Mumbai","Kolkata","Chennai"],"ans":"Delhi"},
    {"id":2,"q":"2+2?","options":["3","4","5","22"],"ans":"4"},
]

leaderboard = []  # list of dicts {"name":..,"score":..}

@app.route("/")
def index():
    return render_template("index.html", questions=QUESTIONS)

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    score = 0
    for q in QUESTIONS:
        ans = request.form.get(str(q["id"]))
        if ans == q["ans"]:
            score += 1
    leaderboard.append({"name":name,"score":score})
    leaderboard.sort(key=lambda x: -x["score"])
    return redirect(url_for("scores"))

@app.route("/scores")
def scores():
    return render_template("scores.html", leaderboard=leaderboard)

if __name__=="__main__":
    app.run(debug=True)
