"""REST API for comments."""
import flask
import backend
import os
from backend.api.yolov5.detect import run
from pathlib import Path


download_file_path = ''
filename = '1.jpg'

@backend.app.route('/api/v1/yolo/', methods=['POST'])
def yolo():
    global download_file_path
    file = flask.request.files['image']
    PATH = Path(__file__).resolve().parent
    PATH = PATH / 'yolov5/data/images'
    for f in os.listdir(PATH):
        os.remove(os.path.join(str(PATH), f))
    file.save(PATH/"1.jpg")
    json_dict = run()
    json_dict["download_file_link"] = '/yolo/download/'
    json_dict['upload_file_link'] = '/yolo/upload/'
    return flask.jsonify(json_dict)


@backend.app.route('/yolo/download/')
def download_file():
	return flask.send_file('./api/yolov5/results/1.jpg', as_attachment=True)

@backend.app.route('/yolo/upload/')
def upload_file():
	return flask.send_from_directory('./api/yolov5/results', '1.jpg')