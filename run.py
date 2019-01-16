from flask import Flask, render_template, request, url_for, session

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/dashboard/<user>')# Some dynamic routing to improve UX
def dashboard(user):
    return render_template('dashboard.html', user=user)

if __name__ == '__main__':
	app.run(debug = True)