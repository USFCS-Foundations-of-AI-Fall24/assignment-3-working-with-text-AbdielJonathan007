import random
#Abd
from Document import *

class Cluster :
    ## a cluster is a group of documents
    def __init__(self, centroid=None, members=None):
        if centroid :
            self.centroid = centroid
        else :
            self.centroid = Document(true_class='pos')
        if members :
            self.members = members
        else :
            self.members = []

    def __repr__(self):
        return f"{self.centroid} {len(self.members)}"

    ## You do this.
    # Document whose tokens counts are the averages
    # Part 2-a) Done 2
    def calculate_centroid(self):
        # Initialize document
        centroid = Document()

        token_counts = {}
        count = 0

        for doc in self.members:
            count += 1
            # tokens in the documents
            for token, value in doc.tokens.items():
                if token not in token_counts:
                    token_counts[token] = 0
                token_counts[token] += value

        for token, total in token_counts.items():
            centroid.tokens[token] = total / count

        return centroid





# Call like so: k_means(2, ['pos','neg'], positive_docs + negative_docs)
# That's next
# check if its right
def k_means(n_clusters, true_classes, data) :
    cluster_list = [Cluster(centroid=Document(true_class=item)) for item in true_classes]

    ## initially assign data randomly.
    data_random = random.sample(data, len(data))

    # Maximum number of iterations
    max_iterations = 10
    i = 0


    ## compute initial cluster centroids

    # while not done and i < limit
    #   i++
    while i < max_iterations:

        new_members = [[] for _ in range(n_clusters)]

        for d in data_random:
            # Find closest cluster centroid based on cosine similarity
            closest_cluster_index = min(range(n_clusters),
                                        key=lambda index: 1 - cosine_similarity(d, cluster_list[index].centroid))
            new_members[closest_cluster_index].append(d)

        # for d in data_random:
        #     closest_cluster_index = min(range(n_clusters),
        #                                 key=lambda index: 1 - cosine_similarity(d, cluster_list[index].centroid))
        #     new_members[closest_cluster_index].append(d)

        # with the closes neighbor

        # Step 4.3: Update centroids for each cluster
        for index, cluster in enumerate(cluster_list):
            if new_members[index]:  # Only update if there are members
                cluster.members = new_members[index]
                cluster.centroid = cluster.calculate_centroid()

        i += 1

    #   reassign each Document to the closest matching cluster using
    #   cosine similarity
    #   compute the centroids of each cluster
    return cluster_list