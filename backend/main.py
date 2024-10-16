from flask import Flask
import os
from blueprints.receipt_manager.analyze_receipt import analyze_receipt_bp
from blueprints.recipe_manager.analyze_recipe import analyze_recipe_bp
from blueprints.recipe_manager.analyze_ingredients import analyze_ingredients_bp

app = Flask(__name__)
app.register_blueprint(analyze_receipt_bp)
app.register_blueprint(analyze_recipe_bp)
app.register_blueprint(analyze_ingredients_bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)