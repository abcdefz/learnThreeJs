#-*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('learnthree.html')
	
@app.route('/cubewithpng', methods=['GET', 'POST'])
def cubeWithPng():
    return render_template('cubewithpng.html')

if __name__ == '__main__':
    app.run(debug=True)