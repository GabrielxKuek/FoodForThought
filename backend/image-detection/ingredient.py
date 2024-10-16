from inference_sdk import InferenceHTTPClient
import os
from dotenv import load_dotenv

load_dotenv()

# define

def ingredient_detection(image_path):
    api_key = os.getenv('ROBOFLOW_APIKEY')

    # code
    CLIENT = InferenceHTTPClient(
        api_url="https://outline.roboflow.com",
        api_key=api_key
    )

    result = CLIENT.infer(image_path, model_id="malaysian-food-recognition-ourez/5")

    return result