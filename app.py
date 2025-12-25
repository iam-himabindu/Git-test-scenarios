import MAC
import windows

import platform
import subprocess
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask running on Linux!"

@app.route("/system-info")
def system_info():
    info = {
        "os_name": os.name,
        "platform": platform.system(),
        "platform_release": platform.release(),
        "current_user": os.getenv("USER"),
        "current_directory": os.getcwd()
    }
    return jsonify(info)

@app.route("/linux-command")
def linux_command():
    # Run a Linux command (e.g., 'uname -a')
    if platform.system() == "Linux":
        result = subprocess.getoutput("uname -a")
        return jsonify({"linux_command_output": result})
    else:
        return jsonify({"error": "Not running on Linux"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
