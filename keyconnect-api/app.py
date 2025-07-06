from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cryptokeys.db'
db = SQLAlchemy(app)

class CryptoKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key_label = db.Column(db.String(100))
    residing_technology = db.Column(db.String(100))

@app.route('/cryptokeys', methods=['GET'])
def get_cryptokeys():
    keys = CryptoKey.query.all()
    return jsonify([
        {"id": k.id, "key_label": k.key_label, "residing_technology": k.residing_technology}
        for k in keys
    ])

if __name__ == '__main__':
    app.run(port=5000, debug=True)