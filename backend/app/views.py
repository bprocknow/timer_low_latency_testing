from flask import request, jsonify
from app import app
from timer import Timer

@app.route('/requestData', methods=['GET'])
def request_data():
    # Here you'll fetch and return the data
    data = {"message": "This is your data"}
    return jsonify(data)

@app.route('/submitResponse', methods=['POST'])
def submit_response():
    # Here you'll handle the response and perform the task
    content = request.json
    # Perform task with the content
    return jsonify({"status": "success"})
