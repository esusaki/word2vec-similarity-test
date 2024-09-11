from gensim.models import KeyedVectors
#import numpy

model = KeyedVectors.load_word2vec_format('word2vec.txt')

print(model.most_similar(positive = ['ミカン'],topn=10))
print(model.most_similar(positive = ['食品'],topn=10))
print(model.most_similar(positive = ['祭'],topn=10))