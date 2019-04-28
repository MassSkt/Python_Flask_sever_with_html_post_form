from flask import Flask, render_template, request,jsonify
from flask_cors import CORS # CORS for Ajax

import json

import numpy as np
from PIL import Image
import io

app = Flask(__name__)
CORS(app) #CORS for Ajax
app.config['UPLOAD_FOLDER'] = './tmp'


@app.route('/')
def hello():
    name = "This is prediction API. Please GET/POST appropriate method"
    return name

@app.route('/good')
def good():
    name = "Good"
    return name

@app.route('/form')
def form():
   return render_template('form.html')

@app.route('/prediction-post', methods=['POST'])
def post_json():
    
    jsn = request.get_json()  # POSTされたJSONを取得
    jsn = request.json  # POSTされたJSONを取得
    print(jsn)
    return jsonify(jsn)  # JSONをレスポンス

@app.route('/prediction-post-file', methods=['POST'])
def post_file():
    print('hello')
    print(request.files)
    if request.files and 'picfile' in request.files:
        print('picfile')
        img = request.files['picfile'].read()
        img = Image.open(io.BytesIO(img))
        img.save('test.jpg')
        img = np.asarray(img) / 255.
        img = np.expand_dims(img, axis=0)
        print(img.shape)
    ret='uploaded'
    return ret  # JSONをレスポンス

@app.route('/confirm', methods = ['POST', 'GET'])
def confirm():
   if request.method == 'POST':
      result = request.form
      js=request.get_json()
      print(result)
      return render_template("confirm.html",result = result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)