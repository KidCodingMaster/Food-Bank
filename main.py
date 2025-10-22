from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)


def read_json(name):
    with open(name, "r") as f:
        data = json.load(f)

        return data


def write_json(name, data):
    with open(name, "w") as f:
        json.dump(data, f, indent=4)


@app.route("/have")
def have():
    return render_template("have_food.html", places=read_json("places.json"))


@app.route("/no", methods=["GET", "POST"])
def add_food():
    if request.method == "POST":
        title = request.form.get("title")
        des = request.form.get("des")
        location = request.form.get("location")
        phone = request.form.get("phone")

        write_json(
            "places.json",
            (
                {title: {"des": des, "location": location, "phone": phone}}
                | read_json("places.json")
            ),
        )

        return redirect(url_for("have"))

    return render_template("add_food.html")


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
