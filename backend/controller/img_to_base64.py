import base64
import os  # Import os to check file existence

# Replace 'your_image.jpg' with the path to your image file
image_path = '../receipt.jpg'
output_file = '../base64_image.txt'

# Check if the image file exists
if not os.path.isfile(image_path):
    print(f"Error: The file {image_path} does not exist.")
else:
    try:
        # Open the image file in binary mode
        with open(image_path, 'rb') as image_file:
            # Read the image file and encode it to base64
            base64_string = base64.b64encode(image_file.read()).decode('utf-8')

        # Write the base64 string to the output text file
        with open(output_file, 'w') as base64_file:
            base64_file.write(base64_string)

        print(f"Base64 string saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
