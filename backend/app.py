from flask import Flask

APP = Flask(__name__)

"""Route to home page"""
@APP.route('/')
def home():
    return "This is Andela..."

if __name__ == '__main__':
    APP.run(debug=True)
