import os
from flask import Flask, render_template, send_from_directory
from article import Blog

blog = Blog()
blog.openArticles()

app = Flask('app')

@app.route('/static/css<path:path>')
def send_js(path):
    return send_from_directory('static/css', path)

@app.route('/', methods=['GET'])
def home():
	return render_template('main.html',
						blog = blog,
						css_file_list = os.listdir('static/css')
					)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.png')

app.run(host=os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
	app.run(debug=False)