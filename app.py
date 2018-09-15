from flask import Flask, render_template, request
import requests
import base64
import sys
import re
import datetime
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
from werkzeug import secure_filename
import os
import json
app = Flask(__name__)
app.config['UPLOAD_FOLDER']='./target'
@app.route('/upload')
def upload_file():
   return render_template('desphoto2.html')  

@app.route('/uploader', methods=['POST'],endpoint='test_upload')
def hello_world():
        
        data1=request.get_json()
        
        print(data1["img_data"],file=sys.stderr)
        #print(type(data1),file=sys.stderr)  
        data=data1["img_data"]
        img_data=str.encode(data)
        #print('Hello world!', file=sys.stderr)
        filepath="./target/"+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
        f=open(filepath,"wb")
        f.write(base64.decodebytes(img_data))
        #return json.dumps({"holla":"bollasa"})

        # Replace <Subscription Key> with your valid subscription key.
        subscription_key = "b41d2e701e644fefad8e3ec994dfe0c9"
        assert subscription_key

        # You must use the same region in your REST call as you used to get your
        # subscription keys. For example, if you got your subscription keys from
        # westus, replace "westcentralus" in the URI below with "westus".
        #
        # Free trial subscription keys are generated in the westcentralus region.
        # If you use a free trial subscription key, you shouldn't need to change
        # this region.
        vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"

        analyze_url = vision_base_url + "describe"

        # Set image_path to the local path of an image that you want to analyze.
        image_path = filepath

        # Read the image into a byte array
        image_data = open(image_path, "rb").read()
        headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
                      'Content-Type': 'application/octet-stream'}
        params     = {'visualFeatures': 'Categories,Description,Color'}
        response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
        response.raise_for_status()

        # The 'analysis' object contains various fields that describe the image. The most
        # relevant caption for the image is obtained from the 'description' property.
        analysis = response.json()
        
        return json.dumps(analysis)
if __name__ == '__main__':
   app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))