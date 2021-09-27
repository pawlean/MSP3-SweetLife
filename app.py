import os
import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html", page_title="Our Recipes")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About Us", company=data)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact Us")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)