import requests
# import libraries for Flask, SQLAlchemy,and Marshmallow (not all methods are used here)
from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#Initialize Flask application as app
app = Flask(__name__)

# Database
# This contains the default config for a local SQLite flat file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mysqlitedb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)

#Serializer to directly return values of object queries from database
# Init Marshmallow
ma = Marshmallow(app)

#Database Class/Model
#Here is the class to create/use the SQL table/columns, a primary key is edit/replace columns as needed
class TABLE(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), primary_key=True)
    food = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return '<%r>' % self.id

# Schema for Marshmallow API Functionality
# fields in the schema should match columns in the db
class TABLESchema(ma.Schema):
    class Meta:
        fields = ('name', 'food')
# Init Schema        
TABLE_schema = TABLESchema()
TABLES_schema = TABLESchema(many=True)        
#App Routes

#Index Route
# Return a web page with a table of users and favorite foods 
# Uses main.css and images in /static
# Uses index.html which extends base.html in /templates
@app.route('/', methods=[ 'GET'])
def index():
    data = TABLE.query.all()
    #return "To use this demo API, go to the URL /api and make a 'GET' Request for additional instruction"
    return render_template('index.html', data=data) 

# API Routes
# API GET/POST directions if a GET, if post check for existing db entries and return error or add to db
@app.route('/api', methods=['GET', 'POST', 'DELETE', 'PUT'])
def api():
    # Provide directions to use API if a GET Request made (READ)
    if request.method == 'GET':
        instructions = { "Make a POST to this URL using a JSON payload like this" : 
                            {"name" : "<yourname>", "food" : "<your_favorite_food>"}
                        }
        return instructions
    # Accept data and add to the Database if POST Request made (CREATE)
    if request.method == 'POST':
        name = request.get_json().get('name', '')
        food = request.get_json().get('food', '')
        check = TABLE.query.filter(TABLE.name == name).all()
        # Duplicate Handling
        if check:
            return {"Error" : "Name already exists"}
        else:
            new_entry = TABLE(name=name, food=food)
            db.session.add(new_entry)
            db.session.commit()
            # Show only the db results for the submitted name
            data = TABLE.query.filter(TABLE.name == name).all()
            # Serialize the db object returned using ma schema
            result = TABLES_schema.dump(data)
            return jsonify(result)
    # Update only existing entries in the Database if PUT Request (UPDATE)            
    if request.method == 'PUT':
        name = request.get_json().get('name', '')
        food = request.get_json().get('food', '')
        #Check for valid entry for name before updating        
        check = TABLE.query.filter(TABLE.name == name).all()
        if check: 
            entry = TABLE.query.get(name)
            entry.food = food
            db.session.commit()
            data = TABLE.query.filter(TABLE.name == name).all()
            # Serialize the db object returned using ma schema
            result = TABLES_schema.dump(data)
            return jsonify(result)
        else:
            return {"Error" : " No entry found for this name. Could not update"}            
    # Delete only existing entries in the Database if DELETE Request (DELETE)
    if request.method == 'DELETE':
        name = request.get_json().get('name', '')
        #Check for valid entry for name before deleting
        check = TABLE.query.filter(TABLE.name == name).all()
        if check:
            entry = TABLE.query.get(name)
            db.session.delete(entry)
            db.session.commit()
            return {"Deleted entry" :  name}
        else:
            return {"Error" : "No entry for this name found to delete"}
 
@app.route('/api/report', methods=['GET'])
def api_report():
            data = TABLE.query.all()
            result = TABLES_schema.dump(data)
            return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)    
