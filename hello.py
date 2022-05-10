from fileinput import filename
from flask import Flask, render_template, request, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Index Page</h1>"


@app.route("/hello")
def hello():
    return "<h1>Hello Page</h1>"


@app.route("/user/<username>")
def show_user_profile(username):
    return f"You are {escape(username)}"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post Id {post_id}"


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return f"SubPath is {escape(subpath)}"


@app.route("/projects/")
def projects():
    return "Projects page"


@app.route("/about")
def about():
    return "About Page"

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        return "Creating Account! Logging You In!"
    else:
        return "Getting User Data! Logging You In!"

@app.route('/welcome/')
@app.route('/welcome/<name>')
def welcome(name=None):
    return render_template('hello.html', name=name)


with app.test_request_context():
    print("\nRoutes:")
    print('Index: ', url_for('index'))
    print('Hello:', url_for('hello'))
    print('Username:', url_for('show_user_profile', username='mahi'))
    print('Post:', url_for('show_post', post_id=2))
    print("Path: ", url_for('show_subpath', subpath='mahi/novice'))
    print("Projects: ", url_for('projects'))
    print("About: ", url_for('about'))
    print("CSS:", url_for('static', filename='style.css'))
    print()
