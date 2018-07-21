"""Flask web server"""
from flask import Flask
from flask import Blueprint
from flask import jsonify
from flask import request

# pylint: disable=bad-whitespace
# pylint: disable=C0301
ENTRIES=[{'id':1, 'title':'That day I Laughed', 'date':'02-07-2018', 'message':'Spicy jalapeno bacon ipsum dolor amet chicken ham hock buffalo short loin pork loin picanha sausage tail frankfurter tenderloin pork belly shankle. Shoulder kielbasa hamburger flank cupim beef bacon. T-bone pork belly leberkas frankfurter beef ribs pig porchetta andouille doner cupim buffalo short loin fatback. Jerky tail burgdoggen short ribs tenderloin shoulder pork loin beef prosciutto cow leberkas brisket strip steak swine hamburger. Beef pork leberkas prosciutto pig landjaeger shankle sirloin tenderloin picanha sausage corned beef jowl. Capicola short ribs filet mignon shoulder ribeye, pastrami hamburger ground round leberkas sirloin meatloaf strip steak. Pork belly beef ribs meatloaf sausage chuck, pancetta pork chop.'}, {'id':2, 'title':'I\'ma Satisfied', 'date':'03-07-2018', 'message':'Relentlessly pursues moth lick the plastic bag. Disappear for four days and return home with an expensive injury; bite the vet. Roll on the floor purring your whiskers off. My slave human didn\'t give me any food so i pooped on the floor purrrrrr yet scamper i am the best but groom yourself 4 hours - checked, have your beauty sleep 18 hours - checked, be fabulous for the rest of the day - checked have my breakfast spaghetti yarn damn that dog . Chew on cable demand to have some of whatever the human is cooking, then sniff the offering and walk away attack the child lounge in doorway. Meoooow dont wait for the storm to pass, dance in the rain meow yet annoy owner until he gives you food say meow repeatedly until belly rubs, feels good for i shredded your linens for you kick up litter. Cats are fats i like to pets them they like to meow back hate dog claw your carpet in places everyone can see - why hide my amazing artistic clawing skills?, hack up furballs lie on your belly and purr when you are asleep yet lick human with sandpaper tongue. Purr for no reason meowwww but have my breakfast spaghetti yarn i\'m going to lap some water out of my master\'s cup meow.'}, {'id':3, 'title':'Cupcakes are smart', 'date':'04-07-2018', 'message':'Cupcake ipsum dolor. Sit amet I love lollipop. Brownie cupcake donut. Powder apple pie jujubes I love marzipan cupcake topping. Lemon drops gummies donut toffee tiramisu cake lollipop tart. Cake caramels chupa chups chocolate cake tiramisu I love marzipan dragée. Ice cream pastry gummies macaroon pudding pastry tootsie roll candy. Sweet roll jelly I love icing chocolate bar. Lemon drops lollipop candy canes chupa chups marzipan tootsie roll. Jelly beans bonbon I love sweet. Tootsie roll candy canes dragée chocolate cake fruitcake candy canes chupa chups. Marshmallow brownie gingerbread. Pudding cake muffin ice cream cupcake. Cotton candy halvah sweet roll fruitcake brownie tootsie roll candy canes cotton candy. Bear claw chupa chups jelly beans cotton candy bonbon bonbon carrot cake. Lemon drops ice cream chocolate. Sweet apple pie sweet roll cookie. Cupcake soufflé danish danish I love tootsie roll cotton candy pastry. Soufflé chupa chups jelly-o carrot cake cake chocolate sugar plum chocolate cake. Powder oat cake pudding jujubes I love marzipan. Bonbon jelly macaroon powder chocolate. Marshmallow I love I love tiramisu tiramisu I love I love icing. Cake gummies tart pie soufflé oat cake pastry. I love I love pastry candy canes bear claw pastry I love.'}]

# Get all routes and link it the app
BP = Blueprint('My_links', __name__)

def create_app():
    """Instantiate the app"""
    app = Flask(__name__)
    app.register_blueprint(BP)
    return app

APP = create_app()

@BP.route('/')
@APP.route('/')
def home_page():
    """Redirect to home screen"""
    # pylint: disable=C0301
    return '<body style="background-color:white; text-align:center;"><h1 style="margin-top:20px; color:pink;">Geetings, Just some lorem ipsum stuff for you...</h1><div style="text-align:center; margin-left: auto; margin-right: auto;  width:500px; padding:10px"><p style="font-size:20px; color:pink;">Ribeye prosciutto corned beef jowl pig tri-tip, buffalo landjaeger short loin hamburger burgdoggen shankle brisket. Buffalo fatback kevin swine. Chicken jerky swine, pastrami ball tip pork boudin jowl pork belly. Pork flank pork loin buffalo porchetta venison beef ribs meatloaf, tail corned beef. Hamburger pork belly ball tip, landjaeger cow swine short ribs flank ham hock shank sirloin ribeye ham pastrami kevin.Does your lorem ipsum text long for something a little meatier? Give our generator a try… it’s tasty!</p><img src="https://img.clipartxtras.com/3708e9dd29786aead4df180fd4977d57_happy-piggy-animal-piglets-and-babies-funny-pig-drawing_600-600.png" alt="Happy me" width=250px height=250px></div></body>'
@BP.route('/api/v1/entries', methods=['GET'])
@APP.route('/api/v1/entries', methods=['GET'])
def get_all_entries():
    """Fetch all entries"""
    return jsonify(ENTRIES)

@BP.route('/api/v1/entries/<int:count>', methods=['GET'])
@APP.route('/api/v1/entries/<int:count>', methods=['GET'])
def get_specific_data(count):
    """Call to get a specific entry"""
    result = [entry for entry in ENTRIES if entry['id'] == count]
    return jsonify(result[0])

@BP.route('/api/v1/entries/<int:count>', methods=['PUT'])
@APP.route('/api/v1/entries/<int:count>', methods=['PUT'])
def put_update_data(count):
    """call to edit an entry"""
    result = [entry for entry in ENTRIES if entry['id'] == count]
    result[0]['title'] = request.json['title']
    result[0]['date'] = request.json['date']
    result[0]['message'] = request.json['message']
    return jsonify(ENTRIES)

@BP.route('/api/v1/entries', methods=['POST'])
@APP.route('/api/v1/entries', methods=['POST'])
def post_data():
    """call to add an entry"""
    new_title = request.json['title']
    new_date = request.json['date']
    new_message = request.json['message']
    new_dict = {'id':len(ENTRIES) + 1, 'title':new_title, 'date':new_date, 'message':new_message}
    ENTRIES.append(new_dict)
    return jsonify(ENTRIES)

if __name__ == '__main__':
    APP.run(debug=True)
