import os
from flask import Flask, render_template, send_from_directory
from article import Blog

blog = Blog()
blog.openArticles()
print(blog.articles)

app = Flask('app')

@app.route('/static/css<path:path>')
def send_js(path):
    return send_from_directory('static/css', path)

@app.route('/')
def home():
	return render_template('main.html',
						blog = blog,
						css_file_list = os.listdir('static/css')
					)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.png')

app.run(host='0.0.0.0', debug=True)