"""Insta485 development configuration."""
import pathlib
# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'
# Secret key for encrypting cookies
SECRET_KEY = b'3u\xca\x16OD\xcd>I\xc8\xc7\xed\x8a\xb9<\x0cS)\
    \xb6\r}\xe3\xee\xbc'

BACKEND_ROOT = pathlib.Path(__file__).resolve().parent.parent
# UPLOAD_FOLDER = INSTA485_ROOT/'var'/'uploads'

YOLO_URL = 'http://35.2.82.78:8000//api/v1/yolo/'