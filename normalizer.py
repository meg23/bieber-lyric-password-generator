

import re

class Normalizer(object):

	def __init__(self, text):
            self.text = text
      
        def convert2password(self):
            text = re.sub(r'\s+', ' ', self.text)
            text = re.sub(r'\W', ' ', text)
            text = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]|]*)\]\]', r'\1', text)
            text = re.sub(r'\([^)]*\)', '', text)
            text = re.sub("\r", " ", text)
            text = re.sub("\n", " ", text)
            text = re.sub("  ", "", text)
            text = re.sub(" ", "_", text)
            return text


