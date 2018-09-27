from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is my home page!'

@app.route('/index')
def index():
    return render_template("index.html",title='Home',name='马牛逼')

@app.route('/page')
def page():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    contents = [
        {'zn':'这是一段中文简介','ch':'this is english brief'},
        {'zn': '这是汉语', 'ch': 'this is english'}
                ]
    return render_template("page.html",
                           title='Home',
                           user=user,
                           posts=posts,
                           contents=contents)

# if __name__ == '__main__':
#     app.run(debug=True)