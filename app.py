import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib as plt

from flask import Flask, render_template
import logging as log

app = Flask(__name__)


def make_wordcloud(text=''):
    wordcloud = WordCloud().generate(text)
    wordcloud.to_file('imgs/test.png')
    log.info('Created WordCloud.')
    return 'Creating WordCloud'

@app.route('/')
def main():
    make_wordcloud()
    return render_template('index.html')

@app.route('/generate.html')
def generate():
    return render_template('generate.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()