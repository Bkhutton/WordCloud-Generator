from flask import Flask, Response, render_template
import logging as log

app = Flask(__name__)

def standard_page(html_file, page_title):
    content = ''

    content = content + render_template('header.html', page_title=page_title)

    with open(html_file) as index:
        content = content + index.read()

    content = content + render_template('footer.html')

    return content

@app.route('/')
def index():
    content = standard_page('index.html', 'Home')
    return Response(content, mimetype='text/html')

@app.route('/generate.html')
def generate():
    content = standard_page('generate.html', 'Generate')
    return Response(content, mimetype='text/html')

@app.route('/about.html')
def about():
    content = standard_page('about.html', 'About')
    return Response(content, mimetype='text/html')

if __name__ == '__main__':
    app.run()