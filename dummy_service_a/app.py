from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "message": "Dummy Service A is running"
    })

if __name__ == '__main__':
    # Run on port 5000 (inside container)
    app.run(host='0.0.0.0', port=5000)