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

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method =='POST':
        users = mongo.db.users
        user_found = users.find_one({'user': request.form['user']})
        if user_found:
            if request.form['password'] == user_found['password']:
                session['user'] = request.form['user']
                return redirect(url_for('index'))
            return render_template('sign_in.html')
        return render_template('sign_in.html')
    return render_template('sign_in.html')

@app.route('/sign_out')
def sign_out():
    session.pop('user')
    return render_template('index.html')

@app.route('/show_recipes')
def show_recipes():
    return render_template('show_recipes.html')

@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
