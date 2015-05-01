'''
Created on 20/apr/2015

@author: Fulvio Corno
'''

from flask import Flask, render_template, request, Response, jsonify
from flask_bootstrap import Bootstrap

from upsidedown import transform

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def processText():
    
    # decode the Json text from the request Body, returns a Python object
    data = request.get_json()
    
    #extract from the Pithon object the fields that we are interested in
    text = data['text']
    
    # process the string
    if data['reverse'] :
        text = text[::-1] 
        # full-lenght slice of the string, with increment -1
        # see https://docs.python.org/2.7/reference/expressions.html#slicings
        # examples at: https://docs.python.org/2.7/whatsnew/2.3.html?highlight=slicing#extended-slices 
        
    if data['flip'] :
        text = transform(text) 

    # build the response object
    result = { 'text': text }
    # return the object in json format
    return jsonify(result)

    # if you don't use jsonify, you must build Json manually
    ## return '{"text":"%s"}' % text
    # or, better, also specify the correct mime type
    ## return Response('{"text":"%s"}' % text, mimetype='application/json')    

if __name__ == '__main__':
    app.run(debug=True)