from inference_sdk import InferenceHTTPClient
import os
from dotenv import load_dotenv

load_dotenv()

# define

api_key = os.getenv('ROBOFLOW_APIKEY')

# code

CLIENT = InferenceHTTPClient(
    api_url="https://outline.roboflow.com",
    api_key=api_key
)

result = CLIENT.infer("lemak.jpg", model_id="malaysian-food-recognition-ourez/5")
