from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"

@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json()
    a = data.get("a", 0)
    b = data.get("b", 0)
    return jsonify({
        "result": a + b
    })

if __name__ == "__main__":
    app.run(debug=True)

