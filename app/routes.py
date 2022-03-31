from flask import request, render_template, redirect
import pyshorteners

from app import app
# from app.controllers import 
# from db_config import get_collection

URL = "http://localhost:5000/"

@app.route("/", methods=["GET", "POST"])
def home():
  if request.method == "GET":
    return render_template('home.html')
  if request.method == "POST":
    long_url = request.form['url-field']
    s = pyshorteners.Shortener()
    tiny_url = s.tinyurl.short(long_url)
    short_url_code = tiny_url.split("/")[-1]
    short_url = URL + short_url_code
    print(short_url)
    return render_template('result.html', url=short_url)
  
# To expand to original URL use .tinyurl.expand(short_url)

@app.route("/<string:path>")
def redirect():
  # Check if it is in the database
  # IF in db redirect
  # else:
  #   return redirect("/")
  pass
