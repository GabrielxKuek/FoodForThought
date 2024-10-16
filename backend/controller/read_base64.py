from flask import Flask, request, jsonify
import base64
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_base64_image():
    base64_file_path = "../base64_image.txt"

    try:
        # # Ensure the request contains a base64 string
        # if 'image_data' not in request.json:
        #     return jsonify({'error': 'No image data provided'}), 400

        # base64_image = request.json['image_data']

        with open(base64_file_path, 'r') as file:
            base64_image = file.read()

        # Decode the Base64 image
        image_data = base64.b64decode(base64_image)

        # Save the image temporarily
        output_file = os.path.join('uploaded_image.jpg')  # Save in the current directory
        with open(output_file, 'wb') as f:
            f.write(image_data)

        # Respond with a success message and the image path
        return jsonify({'message': f'Base64 read and successfully converted into image stored in {output_file}'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
