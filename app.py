import os
from flask import Flask, render_template, send_from_directory
from article import Blog

blog = Blog()
blog.openArticles()
blog.sortArticles()

app = Flask(__name__)

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory('static/css/', filename)

@app.route('/js/<path:filename>')
def js(filename):
	return send_from_directory('static/js', filename)

@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('static/images/', filename)

@app.route('/', methods=['GET'])
def home():
	return render_template('main.html',
						blog = blog,
						css_file_list = os.listdir('static/css'),
						js_file_list = os.listdir('static/js')
					)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.png')

@app.after_request
def set_response_headers(response):
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	response.headers['Pragma'] = 'no-cache'
	response.headers['Expires'] = '0'
	return response

app.run(host=os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)))
if __name__ == '__main__':
	app.run(debug=False)