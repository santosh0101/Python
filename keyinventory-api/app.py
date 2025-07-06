from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/cryptokeys', methods=['GET'])
def proxy_cryptokeys():
    headers = {
        'Authorization': request.headers.get('Authorization'),
        'Id-Token': request.headers.get('Id-Token')
    }
    response = requests.get('http://localhost:5000/cryptokeys', headers=headers)
    if response.status_code != 200:
        return jsonify({"error": "Backend failure"}), response.status_code
    
    # Middleware can filter or transform here
    data = response.json()
    unique_techs = sorted(set(
        item['residing_technology'] for item in data if item.get('residing_technology')
    ))
    return jsonify(unique_techs)

if __name__ == '__main__':
    app.run(port=5001, debug=True)