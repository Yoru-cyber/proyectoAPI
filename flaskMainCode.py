from flask import Flask, render_template, url_for, request, jsonify

urlAPI_Random = 'https://uselessfacts.jsph.pl/'
app = Flask(__name__)
@app.route("/", methods=['GET'])

def home():
    return render_template('index.html')
@app.route('/message', methods=['GET'])
def apiCallTest():
    return jsonify({'message' : '''It's alive'''})

