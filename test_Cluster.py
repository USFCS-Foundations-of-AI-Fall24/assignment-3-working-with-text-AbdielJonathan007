from unittest import TestCase
from Cluster import *
from Document import *

class TestCluster(TestCase):
    # Used chatgpt as a reference to create this test case
    def test_calculate_centroid(self):
        d = Document(true_class='pos')#
        d.add_tokens(['cat', 'dog', 'fish', 'cat']) # cat:2 dog:1 fish:1
        d2 = Document(true_class='pos')
        d2.add_tokens(['cat', 'dog', 'fish']) # cat:1 dog:1 fish:1
        d3 = Document(true_class='pos')
        d3.add_tokens(['fish', 'fish', 'bunny']) #fish 2 bunny:1

        cluster = Cluster()
        cluster.members.extend([d,d2,d3])

        centroid = cluster.calculate_centroid()
        expected_counts = {
            'cat': 1.0,
            'dog': 0.67,  # You can use round to specify how many decimal places you want
            'fish': 1.33,
            'bunny': 0.33
        }

        # Assertions to check if the centroid tokens are as expected
        for token, expected_count in expected_counts.items():
            self.assertAlmostEqual(centroid.tokens.get(token, 0), expected_count, places=2)


    def test_kmeans(self):
        d = Document(true_class='pos')
        d.add_tokens(['cat', 'dog', 'fish'])
        d2 = Document(true_class='pos')
        d2.add_tokens(['cat', 'dog', 'fish'])
        d3 = Document(true_class='neg')
        d3.add_tokens(['bunny', 'lizard', 'octopus'])
        print(k_means(2, ['pos', 'neg'], [d,d2,d3]))


