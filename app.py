from flask import Flask, request, jsonify
import numpy as np
import requests
import cv2
import base64

app = Flask(__name__)

def transform_image(url):
    original_image = requests.get(url)
    
    img_array = np.array(bytearray(original_image.content), dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (500, 500), interpolation=cv2.INTER_AREA)
    
    img_base64 = base64.b64encode(img).decode('utf-8')
    # img_binary = img.tolist()
    
    response = {
        "image": img_base64,
        "message": "Image is BASE 64 encoded"
    }
    
    if img is not None:
        print(response)
        cv2.imshow('ImageWindow', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return response, 200
    else:
        return {"error": "Failed to load image."}, 400

transform_image('https://static8.depositphotos.com/1338574/829/i/950/depositphotos_8292994-stock-photo-the-letter-s-in-gold.jpg')

@app.route('/transform', methods=['POST'])
def image_result():
    data = request.get_json(force=True)
    
    url = data['url']
    
    modify_img = transform_image(url)
    
    return jsonify(modify_img), 200
    
if __name__ == '__main__':
    app.run(debug=True)