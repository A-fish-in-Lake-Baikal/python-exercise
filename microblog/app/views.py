from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is my home page!'
@app.route('/index')
def index():
    return """"""

# if __name__ == '__main__':
#     app.run(debug=True)