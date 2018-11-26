from flask import Flask, flash, redirect, render_template, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer

 
app = Flask(__name__)

def analysetext(processtext):
    sid = SentimentIntensityAnalyzer()
    output = sid.polarity_scores(processtext)
    return output
	
@app.route("/")
def index():
    return render_template('test.html')
		
@app.route("/", methods = ['POST'])	
def result():
    text = request.form['inputText']
    output = analysetext(text)
    return render_template('test.html',output= output)

if __name__ == "__main__":
    app.run()
