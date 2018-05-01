from Athena import getResponse
from flask import Flask, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return send_from_directory('static', "index.html");
@app.route('/<path:path>')
def index(path):
    return send_from_directory('static',path);

@app.route('/chat', methods=["POST"])
def chat():
        json_dict = request.get_json()
        message = json_dict['message']
        return getResponse(message);
if __name__=='__main__':
    app.run(debug=True)