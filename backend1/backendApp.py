from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "About Page"

if __name__ == '__main__':
    app.run()