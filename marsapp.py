from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pandas as pd

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/marsinfo_app"
mongo = PyMongo(app)



@app.route("/")
def index():
    mars_information = mongo.db.mars_information.find_one()
    return render_template("index.html", mars_information=mars_information)


@app.route("/scrape")
def scrape():
    mars_information = mongo.db.mars_information
    mars_data = scrape_mars.scrape_news()
    mars_data = scrape_mars.featured_image()
    mars_data = scrape_mars.weather()
    mars_data = scrape_mars.mars_facts()
    mars_data = scrape_mars.mars_hemisphere()
    mars_information.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
