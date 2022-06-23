from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

TIMEOUT = 540  # in seconds
REDIRECT_URL = 'https://your.host.here/'

if not REDIRECT_URL.endswith('/'):
    REDIRECT_URL += '/'

app = Flask(__name__)
cors = CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if not path:
        return jsonify({'error': 'You need to provide a path'}), 500

    if path == 'favicon.ico':
        return jsonify([]), 404

    args = '&'.join([f"{k}={request.args.get(k)}" for k in request.args])
    args = '?' + args if args else ''
    func = getattr(requests, request.method.lower())
    final_url = REDIRECT_URL + path + args

    try:
        r = func(final_url, timeout=TIMEOUT)
        return jsonify(r.json()), r.status_code
    except Exception as e:
        return jsonify({'exception': repr(e)}), 500


if __name__ == '__main__':
    print(f" * Starting dummy server that redirects requests to host '{REDIRECT_URL}'")
    app.run(host='0.0.0.0', port=15002)
