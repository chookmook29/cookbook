import os
from flask import Flask, render_template, request, url_for, session, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = ']Nk(`K24HLRuRkdN'

app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = 'mongodb://admin:hadvjecbscW2vm4m@ds157834.mlab.com:57834/cookbook'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        user = request.form['user']
        password = request.form['password']
        users.insert({'user': user, 'password': password})
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method =='POST':
        users = mongo.db.users
        user_found = users.find_one({'user': request.form['user']})
        if user_found:
            if (user_found['password'], request.form['password']):
                session['user'] = request.form['user']
                return redirect(url_for('index'))
            return render_template('sign_in.html')
        return render_template('sign_in.html')
    return render_template('sign_in.html')

@app.route('/sign_out')
def sign_out():
    session.clear()
    return render_template('index.html')

@app.route('/show_all')
def show_all():
    recipes = mongo.db.recipes.find()
    return render_template('show_all.html', recipes=recipes)

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        recipes = mongo.db.recipes
        name = request.form['name']
        recipes.insert({'name': name})
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit_recipe', methods=['GET', 'POST'])
def edit_recipe():
    return render_template('edit.html')

@app.route('/delete_recipe', methods=['GET', 'POST'])
def delete_recipe():
    return render_template('delete.html')

@app.route('/show_single/<single_id>')
def show_single(single_id):
    single_recipe = mongo.db.recipes.find_one({"_id": ObjectId(single_id)})
    return render_template('show_single.html', single_recipe=single_recipe)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
