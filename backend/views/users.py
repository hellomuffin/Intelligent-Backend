"""
Insta485 login page view.

URLs include:
/users/<user_url_slug>/
"""


import flask
from werkzeug.exceptions import abort
import backend
import requests

outputs = []

@backend.app.route('/', methods=['GET', 'POST'])
def index():
    """GET /users/<user_url_slug>."""
    if flask.request.method == 'POST':
        options = flask.request.form.getlist('models')
        file = flask.request.files['file']
        if file:
            if 'yolov5' in options:
                url = 'http://35.2.82.78:8000//api/v1/yolo/'
                print("here")
                my_img = {'image': file.stream}
                r = requests.post(url, files=my_img)
                response = r.json()
                response['model_name'] = 'Yolov5'
                response['url'] = url
                outputs.append(response)
            elif 'esrgan' in options:
                pass
            else:
                pass
        return flask.redirect(flask.url_for('show_result'))
    return flask.render_template("index.html")

@backend.app.route('/show/')
def show_result():
    context = {'outputs': outputs}
    return flask.render_template("show.html", **context)