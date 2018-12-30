from flask import Flask, render_template

app = Flask('app')

@app.route('/')
def home():
	return render_template('main.html', article = [('h1','val1'),('h2','val2'),('h3','val3'),('h4','val4')])

app.run(debug=True)