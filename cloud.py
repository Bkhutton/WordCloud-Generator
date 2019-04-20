import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib as plt

import uuid

def generate_text_wordcloud(text, bgcolor, width, height, image):
    id = uuid.uuid1()
    image_path = 'static/imgs/wordcloud_{}.png'.format(id)

    if image is not None:
        mask = np.array(Image.open(image))
        wordcloud = WordCloud(background_color=bgcolor, width=width, height=height, mask=mask)
        wordcloud.generate(text)
        image_colors = ImageColorGenerator(mask)
        wordcloud.recolor(color_func=image_colors)
    else:
        wordcloud = WordCloud(background_color=bgcolor, width=width, height=height)
        wordcloud.generate(text)

    wordcloud.to_file(image_path)
    return image_path

