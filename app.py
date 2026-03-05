from flask import Flask, render_template, request, redirect

app = Flask(__name__)

votes = {
    "Alice": 0,
    "Bob": 0
}

@app.route("/")
def home():
    return render_template("index.html", votes=votes)

@app.route("/vote", methods=["POST"])
def vote():
    candidate = request.form["candidate"]
    votes[candidate] += 1
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)