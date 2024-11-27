# backend/app.py
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import json

app = Flask(__name__, static_folder='../frontend/build')
CORS(app)

# Mock data for demonstration
def get_mock_transactions(wallet_address, contract_address):
    return {
        "nodes": [
            {"data": {"id": "wallet1", "label": "Wallet 1"}},
            {"data": {"id": "wallet2", "label": "Wallet 2"}},
            {"data": {"id": "wallet3", "label": "Wallet 3"}}
        ],
        "edges": [
            {"data": {"source": "wallet1", "target": "wallet2", "label": "100 tokens"}},
            {"data": {"source": "wallet2", "target": "wallet3", "label": "50 tokens"}}
        ]
    }

@app.route('/api/fetch_transactions', methods=['POST'])
def fetch_transactions():
    data = request.json
    wallet_address = data.get('wallet_address')
    contract_address = data.get('contract_address')
    
    if not wallet_address or not contract_address:
        return jsonify({"error": "Wallet and Contract addresses are required"}), 400
    
    # Return mock data for demonstration
    return jsonify(get_mock_transactions(wallet_address, contract_address))

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
