from flask import Flask, request, jsonify, render_template
from utils import scan_all_cookies

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_cookies', methods=['POST'])
def get_all_cookies():
    data = request.get_json()
    url = data.get('url')
    if url:
        cookies = scan_all_cookies(url)
        return jsonify(cookies)
    else:
        return jsonify([])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
