from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('frontend.html')

if __name__ == '__main__':
    app.run()
