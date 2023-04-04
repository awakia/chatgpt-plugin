from flask import Flask, request, jsonify
import plugin

app = Flask(__name__)

@app.route('/transfer', methods=['POST'])
def transfer():
    records = request.json['records']
    success = plugin.append_records_to_spreadsheet(records)
    return jsonify(success=success)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
