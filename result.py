import numpy as np
import os, sys, time
import tensorflow
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from keras.models import load_model
from PIL import Image

# sys.path.insert(1,"/camera")
# basedir = os.path.dirname(__file__)

print("started")

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
  
def loop():

  while True:
    
    folder_path = 'D:\System\Desktop\camera\images'
    filename = os.listdir(folder_path)
    print("scanning")
    if len(filename) == 0:
      while len(filename) == 0:
        filename = os.listdir(folder_path)
        continue
    print(filename)
    file_path = os.path.join(folder_path, str(filename[0]))
    print(file_path)
    pred = pred_cot_dieas(cott_plant=file_path)
    print("Printed Prediction: "+pred)
    os.remove(file_path)
    time.sleep(1)