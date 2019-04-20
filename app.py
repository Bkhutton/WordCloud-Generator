from flask import Flask
from flask import Response
from flask import request
from flask import render_template

import logging as log

from cloud import generate_text_wordcloud

app = Flask(__name__)

def standard_page(html_file,title):
    content = ''

    content = content + render_template('header.html', title=title)

    with open(html_file) as index:
        content = content + index.read()

    #content = content + render_template('footer.html')

    return content

def get_results():
   
    text = request.form['input_text']

    if len(text) < 2:
        results = '<div class="alert alert-danger" role="alert">There were not enough words</div>'
        return results
    
    bgcolor = request.form['bgcolor']

    width = request.form['width']
    if width == '':
        width = 400

    height = request.form['height']
    if height == '':
        height = 200

    if 'file' in request.files:
        mask = request.files['file']
    else:
        mask = None

    image_path = generate_text_wordcloud(text, bgcolor, width, height, mask)
    results = '<img src="{}" alt="{}">'.format(image_path, image_path)
    return results

@app.route('/')
def index():
    content = standard_page('index.html', "Home")
    return Response(content, mimetype='text/html')

@app.route('/generate.html', methods=['POST', 'GET'])
def generate():
    if 'POST' == request.method:
        results = get_results()
    else:
        results = '<p>Results will display here!</p>'

    content = ''

    content = content + render_template('header.html', title='Generate')

    content = content + render_template('generate.html', results=results)
    
    #content = content + render_template('footer.html')

    return Response(content, mimetype='text/html')

@app.route('/about.html')
def about():
    content = standard_page('about.html', 'About')
    return Response(content, mimetype='text/html')

if __name__ == '__main__':
    app.run()