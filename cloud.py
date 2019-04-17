import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib as plt

id = 0

def generate_text_worcloud(user_input):
    wordcloud = WordCloud().generate(user_input)
    image_path = 'imgs/wordcloud_{}.png'.format(id)
    wordcloud.to_file(image_path)