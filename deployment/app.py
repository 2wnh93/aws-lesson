from flask import Flask
from flask import render_template
from flask import request
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# @app.route('/')
# def home():
#     return "Try: http://YOUR_AWS_PUBLIC_URL/api/diabetes?x=0,1,2,3,4,5,6,7,8,9"

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
# expected uri: http://YOUR_AWS_PUBLIC_URL/api/diabetes?x=0,1,2,3,4,5,6,7,8,9
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