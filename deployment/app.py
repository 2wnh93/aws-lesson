# Loads Flask Library
from flask import Flask
# initialises a flask application
app = Flask(__name__)

# used to serve html files
# files have to be inside "templates" folder
from flask import render_template

# handles REST API requests
from flask import request

# loads our model
import pickle


# hello world test
@app.route('/hello') # route defines the API's URI: http://localhost:5000/hello
# function immediately after route will be executed
def hello(): 
    # What the flask server will return
    return "hello world"

# serve website
@app.route('/')
def home():
    # notice that "./index.html" actually means "templates/index.html"
    # this is because render_template() treats 'templates' folder as the root
    return render_template("./index.html")


# load the model
filename = 'finalized_model.sav'
with open(filename, 'rb') as file:
    model = pickle.load(file)

# predicts diabetes
# expected uri: http://localhost:5000/api/diabetes?x=0,1,2,3,4,5,6,7,8,9
@app.route('/api/diabetes')
def diabetes():
    # get the parameter named "x"
    params = request.args.get('x')
    # change "0,1,2,3,4,5,6,7,8,9" to [[0,1,2,3,4,5,6,7,8,9]]
    x = [[float(i) for i in params.split(',')]]
    # use the model to predict
    pred = model.predict(x)[0]
    # sends the prediction back to client
    return str(pred)

# runs the app
if __name__ == '__main__':
  app.run(debug=True)