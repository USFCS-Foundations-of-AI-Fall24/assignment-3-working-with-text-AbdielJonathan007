from unittest import TestCase
from Loader import *


class Test(TestCase):
    def test_apply_filters(self):
        tokens = ['a', 'an', 'the', 'dog', 'cat']
        filtered = [word for word in tokens if not_stopword(word)]
        assert filtered == ['dog', 'cat']

    def test_apply_transforms(self):
        tokens = ['Dog!', 'Cat...', 'Food']
        transformed = [remove_trailing_punct(convert_to_lowercase(word)) for word in tokens]
        assert transformed == ['dog', 'cat', 'food']

# not sure about this test case
def test_workflow():
        pos_reviews, neg_reviews = create_docs(10, 10)

        positive_docs = create_easy_documents(pos_reviews, 'pos',
                                         filters=[not_stopword],
                                         transforms=[convert_to_lowercase, remove_trailing_punct])

        negative_docs = create_easy_documents(neg_reviews, 'neg',
                                              filters=[not_stopword],
                                              transforms=[convert_to_lowercase, remove_trailing_punct])
        assert len(positive_docs) == 10
        assert len(negative_docs) == 10


def test_create_easy_documents():
    assert False


def test_not_stopword(self):
    assert not_stopword('a') == False
    assert not_stopword('an') == False
    assert not_stopword('the') == False
    assert not_stopword('fish') == True


def test_not_cat(self):
    assert not_cat('cat') == False
    assert not_cat('dog') == True


def test_remove_trailing_punct(self):
    assert remove_trailing_punct('hello!') == 'hello'
    assert remove_trailing_punct('world...') == 'world'
    assert remove_trailing_punct('test') == 'test'



def test_convert_to_lowercase(self):
    assert convert_to_lowercase('Cat') == 'cat'
    assert convert_to_lowercase('Dog') == 'dog'
    assert convert_to_lowercase('Fish') == 'fish'
    assert convert_to_lowercase(['Hello', 'WORLD']) == ['hello', 'world']


def test_compute_homogeneity():
    cluster1 = ['pos', 'pos', 'neg', 'pos']
    cluster2 = ['neg', 'neg', 'neg', 'neg']

    classes = ['pos', 'neg']
    expected_results = [0.75, 1.0]
    # compute homogeneity
    result = compute_homogeneity([cluster1, cluster2], classes)

    assert result == expected_results, f"Expected {expected_results} but got {result}"


def test_compute_completeness():
    cluster1 = ['pos', 'neg', 'pos']
    cluster2 = ['pos', 'neg', 'neg']

    classes = ['pos', 'neg']
    expected_results = [2 / 3, 2 / 3]
    # compute homogeneity
    result = compute_homogeneity([cluster1, cluster2], classes)

    assert result == expected_results, f"Expected {expected_results} but got {result}"
