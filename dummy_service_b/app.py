from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    # Simulate a delay and an unhealthy response.
    time.sleep(2)
    return jsonify({
        "status": "unhealthy",
        "message": "Dummy Service B is experiencing issues"
    }), 500

if __name__ == '__main__':
    # Run on port 5000 (inside container)
    app.run(host='0.0.0.0', port=5000)