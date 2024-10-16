from flask import Blueprint, Flask, render_template, request, jsonify
# from controller.yolov10 import detect  # Importing the blueprint for /second
# from controller.read_base64 import read_base64    # Importing the blueprint for /third
import torch
from PIL import Image
import base64
import io


app = Flask(__name__)

# Root route ("/") in the main app file
@app.route('/')
def home():
    return render_template('index.html')

# Register the blueprints for the other routes
# app.register_blueprint(detect, url_prefix='/second')  # "/second"
# app.register_blueprint(read_base64, url_prefix='/third')    # "/third"

model = torch.hub.load(
    'recipe-detection',
    'custom',
    'weights/yolov10b.pt'
)

@app.route('/detect', methods=['POST'])
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

if __name__ == '__main__':
    app.run(debug=True)
