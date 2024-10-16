from flask import Flask
from blueprints.receipt_manager.analyze_receipt import analyze_receipt_bp

app = Flask(__name__)
app.register_blueprint(analyze_receipt_bp)

if __name__ == "__main__":
    app.run(debug=True)