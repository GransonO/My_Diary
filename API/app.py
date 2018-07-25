"""Flask web server"""
from flask import Flask
from flask import Blueprint
from flask_restplus import Api,Resource, fields
from Data import data

dataset = data.dataset.ENTRIES
# Get all routes and link it the app
BP = Blueprint('My_links', __name__)

def create_app():
    """Instantiate the app"""
    app = Flask(__name__)
    app.register_blueprint(BP)
    return app

APP = create_app()
api = Api(APP)

post_detail = api.model('New Entry',{'id': fields.Integer("Enter title"),'message': fields.String("Enter title"),'date': fields.String("Enter title")})
put_detail = api.model('Update Entry',{'title': fields.String("Enter title"),'message': fields.String("Enter title"),'date': fields.String("Enter title")})
#@BP.route('/')
class entries(Resource):
    
    def get(self):
        """Call to get all entries"""
        return dataset
         
    @api.expect(post_detail)
    def post(self):
        """call to add an entry"""
        new_entry = api.payload
        dataset.append(new_entry)
        return {"Total Entries": len(dataset), "All Entries":dataset}

class specific(Resource):
    def get(self,id):
        """Call to get a specific entry"""
        result = [entry for entry in dataset if entry['id'] == id]
        return result[0]

    @api.expect(put_detail)
    def put(self,id):
        """call to edit an entry"""
        sent_data  = api.payload
        result = [entry for entry in dataset if entry['id'] == id]
        result[0]['title'] = sent_data['title']
        result[0]['date'] = sent_data['date']
        result[0]['message'] = sent_data['message']
        return {"result":"Update success"}
    
api.add_resource(entries,'/entries')    
api.add_resource(specific,'/specific/<int:id>')

if __name__ == '__main__':
    from os import environ
    #APP.run(host='0.0.0.0',port=environ.get("PORT", 5000))
    APP.run(host='127.0.0.1',port=environ.get("PORT", 5000),debug=True)
