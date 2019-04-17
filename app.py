from flask import Flask
from flask import Response
from flask import request
from flask import render_template
import logging as log

app = Flask(__name__)

def standard_page(html_file,title):
    content = ''

    content = content + render_template('header.html', title=title)

    with open(html_file) as index:
        content = content + index.read()

    content = content + render_template('footer.html')

    return content

@app.route('/')
def index():
    content = standard_page('index.html', "Home")
    return Response(content, mimetype='text/html')

@app.route('/generate.html', methods=['POST', 'GET'])
def generate():
    if 'POST' == request.method:
        raw_input = request.form['input_text']
        results = raw_input
    else:
        results = 'Results will display here!'

    content = ''

    content = content + render_template('header.html', title='Generate')

    content = content + render_template('generate.html', results=results)
    
    content = content + render_template('footer.html')

    return Response(content, mimetype='text/html')

@app.route('/about.html')
def about():
    content = standard_page('about.html', 'About')
    return Response(content, mimetype='text/html')

if __name__ == '__main__':
    app.run()