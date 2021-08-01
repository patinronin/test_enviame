from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId
import faker
app = Flask(__name__)

client = MongoClient('mongodb://mongodb:27017/')
db = client.test_database

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/users')
def users():
    collection = db.users.find()

    item = {}
    data = []
    for element in collection:
        item = {
            'id': str(element['_id']),
            'name': element['name'],
            'lastname': element['lastname']
        }
        data.append(item)
        jsonify(data=data)
    return render_template('users.html', data=data)

@app.route('/create_user')
def create_user():
    info =''
    name = request.args.get('name')
    lastname = request.args.get('lastname')
    user = {'name': name,'lastname': lastname }
    if name  != None and lastname != None: 
        db.users.insert_one(user)
        info ="Usuario creado"
    return render_template('create_user.html', info=info)

@app.route('/modify_user_action')
def modify_user_action():
    info =''
    id = request.args.get('id')
    name = request.args.get('name')
    lastname = request.args.get('lastname')
    user = {'name': name,'lastname': lastname } 

    if name  != None and lastname != None:
        db.users.update_one({'_id': ObjectId(id)},  {'$set': user}, upsert=False) 
        info =[id,name,lastname]
    return render_template('modify_user.html',info=info)

@app.route('/delete_user')
def delete_user():
    info = ""
    
    id = request.args.get('id')
    if id != None:
        db.users.delete_one({ "_id":ObjectId(id) })
        #uncomment to remove all users 
        #db.users.remove( { } )
        info=[id]
    return render_template('delete_user.html',info=info)





@app.route('/create_fake_user')
def create_fake_user():
    from faker import Faker
    fake = Faker()
    fake_names = fake.name().split() 
    name, lastname= fake_names[0],fake_names[1]
    info =''
    user = {
        'name': name,
        'lastname': lastname
    }
    if name  != None and lastname != None: 
        db.users.insert_one(user)
        info ="Usuario  fake creado"
    return render_template('create_user.html', info=info)


@app.route('/modify_user',methods=['GET', 'POST'])
def modify_user():
    return render_template('modify_user.html')
    


#http://localhost:8000/create_user?name=vanessa&lastname=santoyo
#http://localhost:8000/users
#http://localhost:8000/