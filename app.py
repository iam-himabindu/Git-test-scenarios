iimport os
import flask as plastic

# Create Flask app
app = plastic.Flask(__name__)

# Read an environment variable (example usage of os)
APP_NAME = os.getenv("APP_NAME", "Sample Plastic App")

@app.route("/")
def home():
    content = {
        "app_name": APP_NAME,
        "message": "Hello! This is sample content from a Flask app.",
        "status": "Running successfully"
    }
    return plastic.jsonify(content)

if __name__ == "__main__":
    # Run the app on port 5000
    app.run(host="0.0.0.0", port=5001, debug=True)
