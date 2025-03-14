from flask import Flask, request, Response, jsonify, send_from_directory, abort
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import cv2
import os

app = Flask(__name__)

def transform_image(url):
    original_image = requests.get(url)
    
    img_array = np.array(bytearray(original_image.content), dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img,(500,500),3)
    
    if img is not None:
        cv2.imshow('ImageWindow', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Failed to load image.")

transform_image('https://www.amitai.com/es/wp-content/uploads/2020/06/board-361516_1920.jpg')

# @app.route('/transform', methods=['POST'])
# def image_result():
#     data = request.get_json(force=True)
    
#     url = data['url']
    
#     return transform_image(url)
# transform_image('https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Square_-_black_simple.svg/1200px-Square_-_black_simple.svg.png')
