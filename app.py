from flask import Flask, jsonify,render_template,request
import requests
app = Flask(__name__)
app.config["DEBUG"] = True#only include this while testing

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry, this page was not found.", 404

@app.route("/")
def hello():
	return render_template("search.html")
	
@app.route("/search",methods=["GET","POST"])
def search():
	if request.method == "POST":
        	url = "https://api.github.com/search/repositories?q=" + request.form["user_search"]
        	response_dict = requests.get(url).json()
        	return render_template("results.html",api_data=response_dict)
    	else: # request.method == "GET"
        	return render_template("search.html")

	

@app.route("/name")
def name():
	return "KuiBa"

@app.route("/website")
def website():
	return " <a href='https://www.github.com/actondong'>Github</a>"

if __name__=="__main__":
	app.run(host="0.0.0.0")

