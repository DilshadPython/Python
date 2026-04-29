from sentence_transformers import SentenceTransformer
import numpy as np


'''
This is a sentence-transformers model: It maps sentences & paragraphs to a 384 
dimensional dense vector space and can be used for tasks like clustering or semantic search.
'''
model = SentenceTransformer('all-MiniLM-L6-v2')

# create some example sentences
places = [
    "Beautiful mountains in Kurdistan",
    "Historic citadel in Erbil",
    "Waterfalls in Duhok",
    "Kurdish traditional music"
]

place_vectors = model.encode(places)

def search(query):
    query_vector = model.encode(query)
    cosine_scores = np.dot(query_vector, place_vectors.T)
    best_match_index = np.argmax(cosine_scores)
    return cosine_scores[best_match_index], places[best_match_index]

print(search("nice nature place"))