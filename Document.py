## A representation of a document as a set of tokens.
#Abd
from collections import defaultdict
from math import sqrt

class Document :
    def __init__(self, true_class=None):
        self.true_class = true_class
        self.tokens = defaultdict(lambda:0)

    def add_tokens(self, token_list) :
        for item in token_list :
            self.tokens[item] = self.tokens[item] + 1

    def __repr__(self):
        return f"{self.true_class} {self.tokens}"


# return the distance between two documents
def euclidean_distance(d1, d2) :
    # take the union of the tokens in each document
    union = d1.tokens.keys() | d2.tokens.keys()
    dist = sum([(d1.tokens[item] - d2.tokens[item])**2 for item in union])
    return dist

## You implement this.
# Cos similarity = d1 * d2 / ||d1|| * ||d2||
def cosine_similarity(d1,d2) :
    # calculating the numerator
    num = 0
    for key in d1.tokens:
        # Check if the current key is also in d2
        if key in d2.tokens:
            # If it is, multiply the counts and add to the dot product
            num += d1.tokens[key] * d2.tokens[key]


    # magnitudes
    mag_d1 = 0
    for value in d1.tokens.values():
        mag_d1 += value ** 2
    mag_d1 = sqrt(mag_d1)

    mag_d2 = 0
    for value in d2.tokens.values():
        mag_d2 += value ** 2
    mag_d2 = sqrt(mag_d2)

    # checking if values happen to be zero
    if mag_d1 == 0 or mag_d2 == 0:
        return 0.0

    return num / (mag_d1 * mag_d2)


