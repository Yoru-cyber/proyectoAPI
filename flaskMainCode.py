from flask import Flask, render_template, url_for, request, jsonify
from flask_bootstrap import Bootstrap

urlAPI_Random = 'https://uselessfacts.jsph.pl/'
app = Flask(__name__)
@app.route("/", methods=['GET'])

def home():
    return render_template('home.html')
if __name__ == "__main__":
    app.run(debug=True)
@app.route('/message', methods=['GET'])
def apiCallTest():
    return jsonify({'message' : '''It's alive'''})

