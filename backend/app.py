import os
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)

model = torch.hub.load(
    'recipe-detection',
    'custom',
    'weights/yolov10b.pt'
)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/detect', methods=['POST'])
def detect_objects():
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
    port = int(os.environ.get('PORT', 105))  # Default to 105 if PORT is not set
    app.run(host='0.0.0.0', port=port)
