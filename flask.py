from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/telemetry', methods=['POST'])
def receive_telemetry():
    data = request.json
    print(data)
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
