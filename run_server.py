from flask import Flask
from flask import render_template
from gensim import models
import numpy as np
from operator import itemgetter

app = Flask(__name__)

def get_words(tups, w_list):
	for keys, vals in tups:
		if keys not in w_list:
			w_list.append(keys)
	return w_list

def get_similarities(m1, m2, m3, word, w_n):
	mods = [m1, m2, m3]
	simis = []
	for w in word:
		simis_w = []
		for mos in mods:
			try:
			    val = mos.similarity(w_n, w)
			    simis_w.append(val)
			except:
			    simis_w.append(0)
		simis.append(simis_w)
	return simis
		    

"""
@app.route('/<word_name>')
def load_models(word_name):
 	x = tuple(mod12.most_similar(word_name))
 	y = tuple(mod13.most_similar(word_name))
 	z = tuple(mod14.most_similar(word_name))
 	words = []
 	words = get_words(x, words) 
 	words = get_words(y, words)
 	words = get_words(z, words)
 	similars = get_similarities(mod12, mod13, mod14, words, word_name)
 	varians = map(np.var, similars)
 	pairs = zip(words, similars, varians)	
 
 	pairs.sort(key=itemgetter(2), reverse=True)
 	for i,j,k in pairs:
 		print i, j, k 
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def load_models():
    
    word_name = request.form['interestingtextfield']
    print word_name
    """
    x = tuple(mod12.most_similar(word_name))
    y = tuple(mod13.most_similar(word_name))
    z = tuple(mod14.most_similar(word_name))
    words = []
    words = get_words(x, words) 
    words = get_words(y, words)
    words = get_words(z, words)
    similars = get_similarities(mod12, mod13, mod14, words, word_name)
    varians = map(np.var, similars)
    pairs = zip(words, similars, varians)	

    pairs.sort(key=itemgetter(2), reverse=True)
    for i,j,k in pairs:
        print i, j, k 
    """

mod12 = models.Word2Vec.load('model2012')
mod13 = models.Word2Vec.load('model2013')
mod14 = models.Word2Vec.load('model2014')
app.run()
