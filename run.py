import os
from flask import Flask, render_template, request, url_for, session, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = ']Nk(`K24HLRuRkdN'

app.config['MONGO_DBNAME'] = 'cookbook'
app.config['MONGO_URI'] = 'mongodb://admin:hadvjecbscW2vm4m@ds157834.mlab.com:57834/cookbook'

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
        recipes.insert({
            'creator': session['user'],
            'name': request.form['name'], 
            'image': request.form['image'], 
            'description': request.form['description'],
            'key_ingredient_1': request.form['key_ingredient_1'],
            'key_ingredient_2': request.form['key_ingredient_2'],
            'key_ingredient_3': request.form['key_ingredient_3'],
            'calories': request.form['calories'],
            'time': request.form['time'],
            'serves': request.form['serves'],
            'substitute_1': request.form['substitute_1'],
            'substitute_2': request.form['substitute_2'],
            'voted_list': '',
            'upvotes': '0',
            'downvotes': '0'
            })
        key_ingredient = mongo.db.ingredients
        check_ingredient = key_ingredient.find_one({'key_ingredient' : request.form['key_ingredient_1'].lower()})
        if check_ingredient is None:
                    key_ingredient.insert({'key_ingredient': request.form.get('key_ingredient_1').lower()})
        return redirect(url_for('my_recipes'))
    return render_template('add.html')

@app.route('/my_recipes/')
def my_recipes():
    user = session.get('user')
    my_recipes = mongo.db.recipes.find({'creator': session['user']})
    return render_template('my.html', my_recipes=my_recipes, user=user)

@app.route('/edit_recipe/<edit_id>')
def edit_recipe(edit_id):
    session['edit_id'] = edit_id
    single_edit = mongo.db.recipes.find_one({'_id': ObjectId(edit_id)})
    return render_template('edit.html', single_edit=single_edit)

@app.route('/update_recipe/', methods=['POST'])
def update_recipe():
    edit_id = session.get('edit_id')
    recipes = mongo.db.recipes
    recipes.update(
            {'_id': ObjectId(edit_id)},
            {
                'creator': session['user'],
                'name': request.form['name'], 
                'image': request.form['image'], 
                'description': request.form['description'],
                'key_ingredient_1': request.form['key_ingredient_1'],
                'key_ingredient_2': request.form['key_ingredient_2'],
                'key_ingredient_3': request.form['key_ingredient_3'],
                'calories': request.form['calories'],
                'time': request.form['time'],
                'serves': request.form['serves'],
                'substitute_1': request.form['substitute_1'],
                'substitute_2': request.form['substitute_2'],
                'voted_list': '',
                'upvotes': '0',
                'downvotes': '0'
            })
    return render_template('update.html')

@app.route('/delete/<delete_id>')
def delete_recipe(delete_id):
    single_delete = mongo.db.recipes.remove({'_id': ObjectId(delete_id)})
    return render_template('delete.html', single_delete=single_delete)

@app.route('/show_single/<single_id>')
def show_single(single_id):
    single_recipe = mongo.db.recipes.find_one({'_id': ObjectId(single_id)})
    session['single_id'] = single_id
    creator = list(single_recipe.values())[1]
    session['creator'] = creator
    name = list(single_recipe.values())[2]
    session['name'] = name
    image = list(single_recipe.values())[3]
    session['image'] = image
    description = list(single_recipe.values())[4]
    session['description'] = description
    key_1 = list(single_recipe.values())[5]
    session['key_1'] = key_1
    key_2 = list(single_recipe.values())[6]
    session['key_2'] = key_2
    key_3 = list(single_recipe.values())[7]
    session['key_3'] = key_3
    calories = list(single_recipe.values())[8]
    session['calories'] = calories
    time = list(single_recipe.values())[9]
    session['time'] = time
    serves = list(single_recipe.values())[10]
    session['serves'] = serves
    sub_1 = list(single_recipe.values())[11]
    session['sub_1'] = sub_1
    sub_2 = list(single_recipe.values())[12]
    session['sub_2'] = sub_2
    voted_list = list(single_recipe.values())[13]
    session['voted_list'] =  voted_list
    upvotes = list(single_recipe.values())[14]
    session['upvotes'] = upvotes
    downvotes = list(single_recipe.values())[15]
    session['downvotes'] = downvotes
    return render_template('show_single.html', single_recipe=single_recipe)

@app.route('/upvote_recipe/', methods=['POST'])
def upvote_recipe():
    single_id = session.get('single_id')
    voted_list = session.get('voted_list')
    user = session.get('user')
    voted_list = str(voted_list)
    if user in voted_list:  
        return render_template('already_voted.html')
    else:
        upvotes =  session.get('upvotes')
        upvotes = int(upvotes)
        upvotes = upvotes + 1
        upvotes = str(upvotes)
        voted_list = voted_list + user
        recipes = mongo.db.recipes
        recipes.update(
                {'_id': ObjectId(single_id)},
                {
                    'creator': session['creator'],
                    'name': session['name'], 
                    'image': session['image'], 
                    'description': session['description'],
                    'key_ingredient_1': session['key_1'],
                    'key_ingredient_2': session['key_2'],
                    'key_ingredient_3': session['key_3'],
                    'calories': session['calories'],
                    'time': session['time'],
                    'serves': session['serves'],
                    'substitute_1': session['sub_1'],
                    'substitute_2': session['sub_2'],
                    'voted_list': voted_list,
                    'upvotes': upvotes,
                    'downvotes': session['downvotes']
                })
        return render_template('upvote.html')


@app.route('/downvote_recipe/', methods=['POST'])
def downvote_recipe():
    single_id = session.get('single_id')
    voted_list = session.get('voted_list')
    user = session.get('user')
    voted_list = str(voted_list)
    if user in voted_list:  
        return render_template('already_voted.html')
    else:
        downvotes =  session.get('downvotes')
        downvotes = int(downvotes)
        downvotes = downvotes + 1
        downvotes = str(downvotes)
        voted_list = voted_list + user
        recipes = mongo.db.recipes
        recipes.update(
                {'_id': ObjectId(single_id)},
                {
                    'creator': session['creator'],
                    'name': session['name'], 
                    'image': session['image'], 
                    'description': session['description'],
                    'key_ingredient_1': session['key_1'],
                    'key_ingredient_2': session['key_2'],
                    'key_ingredient_3': session['key_3'],
                    'calories': session['calories'],
                    'time': session['time'],
                    'serves': session['serves'],
                    'substitute_1': session['sub_1'],
                    'substitute_2': session['sub_2'],
                    'voted_list': voted_list,
                    'upvotes': session['upvotes'],
                    'downvotes': downvotes
                })
        return render_template('downvote.html')

@app.route('/by_ingredient/')
def by_ingredient():
    return render_template('ingredient.html', key_ingredient=mongo.db.ingredients.find())

@app.route('/ingredient_recipes/<key_ingredient>')
def ingredient_recipes(key_ingredient):
    recipes_total = mongo.db.recipes.find({'key_ingredient_1': key_ingredient}).count()
    return render_template('single_ingredient.html', recipes=mongo.db.recipes.find({'key_ingredient_1': key_ingredient}), recipes_total=recipes_total)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
