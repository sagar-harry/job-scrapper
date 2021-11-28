from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from scraper import scrape


app = Flask(__name__)

@app.route("/")
def method1():
    jobs = scrape() 
    return render_template("index.html", jobs=jobs)


if __name__=="__main__":
    app.run(debug=True)