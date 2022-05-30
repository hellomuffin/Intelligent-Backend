import requests

url = 'http://localhost:8000/api/v1/yolo/'
my_img = {'image': open('test.jpg', 'rb')}
r = requests.post(url, files=my_img)

# convert server response into JSON format.
print(r.json())