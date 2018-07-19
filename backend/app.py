"""Flask web server"""
from flask import Flask

APP = Flask(__name__)

@APP.route('/')
def home_page():
    """Redirect to home screen"""
    return '<body style="background-color:white; text-align:center;"><h1 style="margin-top:20px; color:pink;">Geetings, Just some lorem ipsum stuff for you...</h1><div style="text-align:center; margin-left: auto; margin-right: auto;  width:500px; padding:10px"><p style="font-size:20px; color:pink;">Ribeye prosciutto corned beef jowl pig tri-tip, buffalo landjaeger short loin hamburger burgdoggen shankle brisket. Buffalo fatback kevin swine. Chicken jerky swine, pastrami ball tip pork boudin jowl pork belly. Pork flank pork loin buffalo porchetta venison beef ribs meatloaf, tail corned beef. Hamburger pork belly ball tip, landjaeger cow swine short ribs flank ham hock shank sirloin ribeye ham pastrami kevin.Does your lorem ipsum text long for something a little meatier? Give our generator a try… it’s tasty!</p><img src="https://img.clipartxtras.com/3708e9dd29786aead4df180fd4977d57_happy-piggy-animal-piglets-and-babies-funny-pig-drawing_600-600.png" alt="Happy me" width=250px height=250px></div></body>'

if __name__ == '__main__':
    APP.run(debug=True)
