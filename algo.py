from flask import Flask,render_template, jsonify, make_response,abort, url_for, request
from joblib import load
import os

app = Flask(__name__)
port = int(os.environ.get("PORT",5000))

@app.route('/predict',methods=['GET'])
def predict():
    """ Prediction """
    clf = load("algo_classes.joblib")
    sentence = [request.args.get("tweet")]
    print(type(sentence))
    predict_value = clf.predict(sentence)
    print(predict_value)
    return render_template("tweet.jinja2", result=predict_value[0])

@app.route('/')
def index():
	return render_template('tweet.jinja2')

#run at http://0.0.0.0:5000
if __name__ == "__main__":        
    app.run(debug=True,host='0.0.0.0',port=port)
