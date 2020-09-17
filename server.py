from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('mainPage.html')


@app.route('/new')
def CreateNew():
    return "helloworld"

if __name__== '__main__':
    app.run()