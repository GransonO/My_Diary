from flask import Flask

app = Flask(__name__)

"""Call to get all entries"""
@app.route('/api/v1', methods=['GET'])
def get_data():
    return "This is GET..."

"""Call to get a specific entry"""
@app.route('/api/v1/<string:name>', methods=['GET'])
def get_specific_data(name):
    return "This is SPECIFIC GET..." + name

"""call to add an entry"""
@app.route('/api/v1', methods=['POST'])
def post_data():
    return "This is POST..."

"""call to edit an entry"""
@app.route('/api/v1/<string:user>', methods=['PUT'])
def put_data(user):
    return "This is PUT..." + user

if __name__ == '__main__':
    app.run(debug=True)
