import os
from flask import Flask, request, jsonify
import torch
import base64
import io
from PIL import Image

app = Flask(__name__)

model = torch.hub.load(
    '../recipe-detection',
    'custom',
    '../weights/yolov10b.pt'
)

@app.route('/', methods=['POST'])
def detect():
    data = request.json
    if 'image' not in data:
        return jsonify({'error': 'No image provided'}), 400
    
    # Decode base64 image
    img_data = base64.b64decode(data['image'])
    img = Image.open(io.BytesIO(img_data))
    
    # Perform detection
    results = model(img)
    
    # Process results
    detections = results.pandas().xyxy[0].to_dict(orient="records")
    
    return jsonify({'detections': detections})