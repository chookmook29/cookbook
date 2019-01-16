from flask import Flask, render_template, request, url_for, session

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/dashboard/<user>')# Some dynamic routing to improve UX
def dashboard(user):
    return render_template('dashboard.html', user=user)

@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')

@app.route('/sign_out')
def sign_out():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/show_recipes')
def show_recipes():
    return render_template('show_recipes.html')

@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html')

if __name__ == '__main__':
	app.run(debug = True)