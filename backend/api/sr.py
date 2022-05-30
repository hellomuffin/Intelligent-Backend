import flask
import backend
import os
from pathlib import Path
import subprocess
import time


filename = '1.jpg'

@backend.app.route('/api/v1/sr/', methods=['POST'])
def sr():
    file = flask.request.files['image']
    PATH = Path(__file__).resolve().parent
    PATH = PATH / 'sr/inputs'
    for f in os.listdir(PATH):
        os.remove(os.path.join(str(PATH), f))
    file.save(PATH/"1.jpg")
    
    start = time.time()
    os.chdir('./backend/api/sr')
    cmd = ['./superresolution', '-i','inputs/1.jpg','-o','outputs/1.jpg']
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    os.chdir('../../..')
    end = time.time()
    
    exe_time = end - start
    
    json_dict = {'latency': f'{exe_time}s', 'result':'None'}
    json_dict["download_file_link"] = '/sr/download/'
    json_dict['upload_file_link'] = '/sr/upload/'
    return flask.jsonify(json_dict)


@backend.app.route('/sr/download/')
def download_file():
	return flask.send_file('./api/sr/inputs/1.jpg', as_attachment=True)

@backend.app.route('/sr/upload/')
def upload_file():
	return flask.send_from_directory('./api/sr/outputs', '1.jpg')