from flask import Flask, request
import sys, os, time

import threading
import result

import numpy as np
import os, sys, time
import tensorflow
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from keras.models import load_model
from PIL import Image

sys.path.insert(1,"/camera")
basedir = os.path.dirname(__file__)


app = Flask(__name__)

ip_address_of_camera = ""

model = load_model('pblproject6.h5')
def pred_cot_dieas(cott_plant):
  test_image = load_img(cott_plant, target_size = (150, 150)) # load image 
  # print("@@ Got Image for prediction")
   
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
   
  result = model.predict(test_image).round(3) # predict diseased palnt or not
  # print('@@ Raw result = ', result)
   
  pred = np.argmax(result) # get the index of max value
  # print(pred)
  if pred == 0:
    return "Diseased Cotton Plant"
  elif pred == 1:
      return 'Diseased Cotton Plant'
  elif pred == 2:
      return 'Healthy Cotton Plant'
  else:
    return "Healthy Cotton Plant"

image_counter = 0

@app.route('/save_image', methods=['POST'])
def save_image():
    # Get the image data from the request
    image_data = request.data
    global image_counter
    image_counter += 1
    # Save the image to a file
    file_path = basedir + '\images\image' +str(image_counter)+'.jpg' 
    with open(file_path, 'wb') as f:
        f.write(image_data)
        global pred
        pred = pred_cot_dieas(cott_plant=file_path)
        print(pred)
    
    os.remove(file_path)

    return pred

@app.route('/save_ip', methods=['POST'])
def save_ip():
    # print("in it")
    # Get the image data from the request
    global ip_address_of_camera
    ip_address_of_camera = request.data.decode('utf-8')
    print(ip_address_of_camera)

    return 'IP saved'


@app.route('/get_ip')
def get_ip():
    print("_______________________Sending ip___________________________")
    return ip_address_of_camera

@app.route('/get_result')
def get_result():
    print("_______________________Sending result___________________________")
    return pred

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    