from flask import Flask, request, jsonify, send_from_directory
import plugin


DEBUG = True
app = Flask(__name__, static_url_path="", static_folder="static")

@app.route('/ping')
def ping():
    return "pong"


@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    records = request.json['records']
    success = plugin.append_records_to_spreadsheet(records)
    return jsonify(success=success)

@app.route('/.well-known/<path:filename>')
def custom_static(filename):
    return send_from_directory('.well-known', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=DEBUG)
