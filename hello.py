from flask import Flask, make_response, redirect, render_template, request, url_for, abort, jsonify
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return f"<h1>Index Page and These are the args passed in {request.args}</h1>"


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


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Creating Account! Logging You In!"
    else:
        return "Getting User Data! Logging You In!"


@app.route('/welcome/')
@app.route('/welcome/<name>')
def welcome(name=None):
    return render_template('hello.html', name=name)


@app.route('/redirect_me')
def redirect_me():
    return redirect(url_for('index'))


@app.route('/cookie')
def cookie():
    response = make_response(render_template('hello.html', name='Maheshkumar'))
    response.set_cookie('username', 'Maheshkumar')
    response.set_cookie('this_is', 'another cookie')
    response.headers['Hi'] = 'Im a header'
    return response


@app.route('/show_cookie')
def show_cookie():
    return request.cookies


@app.route('/abort_me')
def abort_me():
    abort(401)

@app.route('/json_api')
def json_api():
    return {'my_fav_language1': 'ruby :)', 'my_fav_language2': 'python ;)'}

@app.route('/list_json_api')
def list_json_api():
    return jsonify(['hi', {'hi': 'yo'}, ['hiya']])

@app.errorhandler(401)
def unauthorized(error):
    return "<h1>This is a decorated page for Aborting with 401 code", 401


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
