import os
from flask import Flask, render_template, request
from flask import url_for, session, redirect, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import boto3


app = Flask(__name__)
app.secret_key = ']Nk(`K24HLRuRkdN'

app.config['MONGO_DBNAME'] = 'cookbook'
app.config['MONGO_URI'] = \
    'mongodb://admin:hadvjecbscW2vm4m@ds157834.mlab.com:57834/cookbook'
S3_BUCKET = 'uploadscookbook'
S3_KEY = os.environ.get('S3_KEY')
S3_SECRET = os.environ.get('S3_SECRET')
S3_LOCATION = 'http://uploadscookbook.s3.amazonaws.com/'

s3 = boto3.client(
    "s3",
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET
)


def upload_file_to_s3(file, bucket_name):
    try:
        s3.upload_fileobj(file, bucket_name, file.filename)
    except Exception as e:
        return e
    return "{}{}".format(S3_LOCATION, file.filename)


def update():
    voted_up = session.get('voted_up')
    voted_down = session.get('voted_down')
    downvotes = session.get('downvotes')
    upvotes = session.get('upvotes')
    single_id = session.get('single_id')
    recipes = mongo.db.recipes
    recipes.update(
                {'_id': ObjectId(single_id)},
                {
                    'creator': session['creator'],
                    'name': session['name'],
                    'image': session['image'],
                    'description': session['description'],
                    'key_ingredient_1': session['key_1'],
                    'calories': session['calories'],
                    'time': session['time'],
                    'serves': session['serves'],
                    'substitute_1': session['sub_1'],
                    'voted_up': voted_up,
                    'voted_down': voted_down,
                    'upvotes': upvotes,
                    'downvotes': downvotes
                })

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
        session['user'] = request.form['user']
        return redirect(url_for('index'))
    return render_template('register.html')


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        users = mongo.db.users
        user_found = users.find_one({'user': request.form['user']})
        if user_found:
            if (user_found['password'] == request.form['password']):
                session['user'] = request.form['user']
                flash('You were successfully signed in')
                return redirect(url_for('index'))
            return render_template('sign_in.html')
        return render_template('sign_in.html')
    return render_template('sign_in.html')


@app.route('/sign_out')
def sign_out():
    flash('You were successfully signed out')
    session.clear()
    return redirect(url_for('index'))


@app.route('/show_all')
def show_all():
    recipes = mongo.db.recipes.find()
    return render_template('show_all.html', recipes=recipes)


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        file = request.files["image"]
        output = upload_file_to_s3(file, S3_BUCKET)
        recipes = mongo.db.recipes
        recipes.insert({
            'creator': session['user'],
            'name': request.form['name'].lower(),
            'image': output,
            'description': request.form['description'],
            'key_ingredient_1': request.form['key_ingredient_1'].lower(),
            'calories': request.form['calories'],
            'time': request.form['time'],
            'serves': request.form['serves'],
            'substitute_1': request.form['substitute_1'],
            'voted_up': '',
            'voted_down': '',
            'upvotes': '0',
            'downvotes': '0'
            })
        key_ingredient = mongo.db.ingredients
        check_ingredient = key_ingredient\
            .find_one({'key_ingredient': request.form['key_ingredient_1']
                      .lower()})
        if check_ingredient is None:
            key_ingredient\
                .insert({'key_ingredient': request.form.get('key_ingredient_1')
                        .lower()})
        flash('Recipe added')
        return redirect(url_for('my_recipes'))
    return render_template('add.html')


@app.route('/my_recipes/')
def my_recipes():
    user = session.get('user')
    my_recipes_count = mongo.db.recipes.find({'creator': session['user']})\
        .count()
    my_recipes = mongo.db.recipes.find({'creator': session['user']})
    if my_recipes_count == 0:
        return render_template('no_results.html')
    else: 
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
                'name': request.form['name'].lower(),
                'image': request.form['image'],
                'description': request.form['description'],
                'key_ingredient_1': request.form['key_ingredient_1'].lower(),
                'calories': request.form['calories'],
                'time': request.form['time'],
                'serves': request.form['serves'],
                'substitute_1': request.form['substitute_1'],
                'voted_up': '',
                'voted_down': '',
                'upvotes': '0',
                'downvotes': '0'
            })
    flash('Recipe updated')
    return redirect(url_for('my_recipes'))


@app.route('/delete/<delete_id>')
def delete_recipe(delete_id):
    single_delete = mongo.db.recipes.remove({'_id': ObjectId(delete_id)})
    flash('Recipe deleted')
    return redirect(url_for('my_recipes'))


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
    calories = list(single_recipe.values())[6]
    session['calories'] = calories
    time = list(single_recipe.values())[7]
    session['time'] = time
    serves = list(single_recipe.values())[8]
    session['serves'] = serves
    sub_1 = list(single_recipe.values())[9]
    session['sub_1'] = sub_1
    voted_up = list(single_recipe.values())[10]
    session['voted_up'] = voted_up
    voted_down = list(single_recipe.values())[11]
    session['voted_down'] = voted_down
    upvotes = list(single_recipe.values())[12]
    session['upvotes'] = upvotes
    downvotes = list(single_recipe.values())[13]
    session['downvotes'] = downvotes
    return render_template('show_single.html', single_recipe=single_recipe)


@app.route('/upvote_recipe/<single_id>')
def upvote_recipe(single_id):
    single_id = session.get('single_id')
    voted_up = session.get('voted_up')
    voted_down = session.get('voted_down')
    downvotes = session.get('downvotes')
    upvotes = session.get('upvotes')
    user = session.get('user')
    voted_up = str(voted_up)
    voted_down = str(voted_down)
    if user in voted_up:
        return render_template('show_single.html',
                               single_recipe=mongo.db.recipes
                               .find_one({'_id': ObjectId(single_id)}))
    elif user in voted_down:
        downvotes = int(downvotes)
        downvotes = downvotes - 1
        downvotes = str(downvotes)
        voted_down = voted_down.replace(user, "")
        upvotes = int(upvotes)
        upvotes = upvotes + 1
        upvotes = str(upvotes)
        voted_up = voted_up + user
        session['voted_up'] = voted_up
        session['voted_down'] = voted_down
        session['upvotes'] = upvotes
        session['downvotes'] = downvotes
        update()
        return render_template('show_single.html',
                               single_recipe=mongo.db.recipes
                               .find_one({'_id': ObjectId(single_id)}))
    else:
        upvotes = int(upvotes)
        upvotes = upvotes + 1
        upvotes = str(upvotes)
        voted_up = voted_up + user
        session['voted_up'] = voted_up
        session['upvotes'] = upvotes
        recipes = mongo.db.recipes
        recipes.update(
                {'_id': ObjectId(single_id)},
                {
                    'creator': session['creator'],
                    'name': session['name'],
                    'image': session['image'],
                    'description': session['description'],
                    'key_ingredient_1': session['key_1'],
                    'calories': session['calories'],
                    'time': session['time'],
                    'serves': session['serves'],
                    'substitute_1': session['sub_1'],
                    'voted_up': voted_up,
                    'voted_down': voted_down,
                    'upvotes': upvotes,
                    'downvotes': session['downvotes']
                })
        return render_template('show_single.html',
                               single_recipe=mongo.db.recipes
                               .find_one({'_id': ObjectId(single_id)}))


@app.route('/downvote_recipe/<single_id>')
def downvote_recipe(single_id):
    single_id = session.get('single_id')
    voted_down = session.get('voted_down')
    voted_up = session.get('voted_up')
    downvotes = session.get('downvotes')
    upvotes = session.get('upvotes')
    user = session.get('user')
    voted_down = str(voted_down)
    voted_up = str(voted_up)
    if user in voted_down:
        return render_template('show_single.html',
                               single_recipe=mongo.db.recipes
                               .find_one({'_id': ObjectId(single_id)}))
    elif user in voted_up:
        downvotes = int(downvotes)
        downvotes = downvotes + 1
        downvotes = str(downvotes)
        voted_down = voted_down + user
        upvotes = int(upvotes)
        upvotes = upvotes - 1
        upvotes = str(upvotes)
        voted_up = voted_up.replace(user, "")
        session['voted_up'] = voted_up
        session['voted_down'] = voted_down
        session['upvotes'] = upvotes
        session['downvotes'] = downvotes
        update()
        return render_template('show_single.html',
                               single_recipe=mongo.db.recipes
                               .find_one({'_id': ObjectId(single_id)}))
    else:
        downvotes = int(downvotes)
        downvotes = downvotes + 1
        downvotes = str(downvotes)
        voted_down = voted_down + user
        session['voted_down'] = voted_down
        session['downvotes'] = downvotes
        recipes = mongo.db.recipes
        recipes.update(
                {'_id': ObjectId(single_id)},
                {
                    'creator': session['creator'],
                    'name': session['name'],
                    'image': session['image'],
                    'description': session['description'],
                    'key_ingredient_1': session['key_1'],
                    'calories': session['calories'],
                    'time': session['time'],
                    'serves': session['serves'],
                    'substitute_1': session['sub_1'],
                    'voted_up': voted_up,
                    'voted_down': voted_down,
                    'upvotes': session['upvotes'],
                    'downvotes': downvotes
                })
        return render_template('show_single.html',
                               single_recipe=mongo.db.recipes
                               .find_one({'_id': ObjectId(single_id)}))


@app.route('/by_ingredient/')
def by_ingredient():
    ingredient_list = []
    counted_ingredients = {}
    for x in mongo.db.ingredients.find({}, {"_id": 0, "key_ingredient": 1}):
        y = x['key_ingredient']
        ingredient_list.append(y)
    for n in ingredient_list:
        m = mongo.db.recipes.find({"key_ingredient_1": n}).count()
        if m == 0:
            continue
        else:
            counted_ingredients[n] = m
    contributors_list = []
    counted_contributors = {}
    for u in mongo.db.recipes.find({}, {"creator": 1}):
        w = u['creator']
        contributors_list.append(w)
    for o in contributors_list:
        p = mongo.db.recipes.find({"creator": o}).count()
        if p == 0:
            continue
        else:
            counted_contributors[o] = p
    return render_template('ingredient.html',
                           key_ingredient=mongo.db.ingredients.find()
                           .sort("key_ingredient", 1),
                           counted_ingredients=counted_ingredients,
                           counted_contributors=counted_contributors)


@app.route('/by_search/', methods=['POST'])
def by_search():
    if request.form['search'] == "":
        return render_template('no_results.html')
    else:
        search = request.form['search'].lower()
        recipes_total = mongo.db.recipes\
            .find({'name': {"$regex": search}}).count()
        recipes = mongo.db.recipes.find({'name': {"$regex": search}})
        if recipes_total > 0:
            return render_template('name.html',
                                   recipes=recipes,
                                   recipes_total=recipes_total)
        else:
            return render_template('no_results.html')


@app.route('/ingredient_recipes/<key_ingredient>')
def ingredient_recipes(key_ingredient):
    recipes_total = mongo.db.recipes\
        .find({'key_ingredient_1': key_ingredient}).count()
    return render_template('single_ingredient.html',
                           recipes=mongo.db.recipes
                           .find({'key_ingredient_1': key_ingredient}),
                           recipes_total=recipes_total,
                           key_ingredient=key_ingredient)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
