from flask import Flask , render_template , request

app = Flask(__name__)
 
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def initial():
    # render the initial main page
    return render_template('index.html',
                           title = 'NLP - Text input')
