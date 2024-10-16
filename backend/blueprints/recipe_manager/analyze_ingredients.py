from flask import Blueprint, request, jsonify
from inference_sdk import InferenceHTTPClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Blueprint
analyze_ingredients_bp = Blueprint('analyze_ingredients', __name__, template_folder='templates')

# Ingredient detection function
def ingredient_detection(image_path):
    api_key = os.getenv('ROBOFLOW_APIKEY')

    # Initialize the client
    CLIENT = InferenceHTTPClient(
        api_url="https://outline.roboflow.com",
        api_key=api_key
    )

    # Perform inference on the image
    result = CLIENT.infer(image_path, model_id="grocery-products-detection/5")
    
    # Return the result
    return result

# Endpoint to handle ingredient analysis requests
@analyze_ingredients_bp.route('/analyze_ingredients', methods=['POST'])
def analyze_ingredients():
    # Check if the request has a file or URL
    if 'image_url' in request.json:
        image_url = request.json['image_url']
        try:
            # Call the ingredient detection function with the image URL
            result = ingredient_detection(image_url)
            return jsonify({"status": "success", "result": result}), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
    else:
        return jsonify({"status": "error", "message": "No image URL provided."}), 400
