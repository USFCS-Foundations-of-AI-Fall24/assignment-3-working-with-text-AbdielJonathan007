## Code for loading training sets and creating documents.
import string
#Abd
from Document import *
from Cluster import *
from make_dataset import create_docs


# you should be able to call this like:
# positive_docs = create_easy_documents(pos_reviews, 'pos',
#                                  filters=[not_stopword],
#                                  transforms=[convert_to_lowercase, remove_trailing_punct])

def create_easy_documents(list_of_docs, true_class, filters=None, transforms=None) :
    document_list = []
    for item in list_of_docs :
        d = Document(true_class=true_class)
        words = item
        ## deal with filters here
        for f in filters:
            words = [word for word in words if f(word)]

        ## deal with transforms here
        # Applying transforms
        for t in transforms:
            words = [word for word in words if t(word)]


        d.add_tokens(words)
        document_list.append(d)
    return document_list

## filters - return true if the token meets the criterion

# you do this.
def not_stopword(token) :
    stop_words = ['a','an','the']
    return token not in stop_words

# return token is not 'cat'
def not_cat(token) :
    return token != 'cat'


# transforms - convert a token into a new format

# you do this.
# not sure if its right
# Used chatgpt as reference here
def remove_trailing_punct(token) :
    return token.rstrip(string.punctuation)

# and this
def convert_to_lowercase(token):
    return token.lower()




## homogeneity: for each cluster, what fraction of the cluster is comprised of the largest class?
# call this like so:
# result = k_means(2, ['pos','neg'], positive_docs + negative_docs)
# compute_homogeneity(result, ['pos','neg'])
def compute_homogeneity(list_of_clusters, list_of_classes) :
    # hlist will be the homogeneity for each cluster.
    hlist = []

    for cluster in list_of_clusters:
        cluster_count = {}
        total_samples = len(cluster)

        for sample in cluster:
            if sample in list_of_classes:
                if sample in cluster_count:
                    cluster_count[sample] += 1
                else:
                    cluster_count[sample] = 1
        # Finding the count of the largest class
        largest_count = max(cluster_count.values(), default=0)

        # Calculating the homogenity for each cluster
        if total_samples > 0:
            homogeneity = largest_count / total_samples
        else :
            homogeneity = 0

        hlist.append(homogeneity)

    return hlist

## completeness: for the dominant class in each cluster, what fraction
# of that class' members are in that cluster?
# call this like so:
# result = k_means(2, ['pos','neg'], positive_docs + negative_docs)
# compute_completeness(result, ['pos','neg'])
# Make some changes on this function
def compute_completeness(list_of_clusters, list_of_classes):
    # clist will be the homogeneity for each cluster.
    clist = []

    total_class_count = 0
    for cls in list_of_classes:
        total_class_count[cls] = 0
    # completeness of each cluster


    for cluster in list_of_clusters:
        for sample in cluster:
            if sample in total_class_count:
                total_class_count[sample] += 1


    for cluster in list_of_clusters:
        cluster_count = {}

        # Counting instances of each cluster
        for sample in cluster:
            if sample in list_of_classes:
                if sample in cluster_count:
                    cluster_count[sample] += 1
                else:
                    cluster_count[sample] = 1

        # Determining the dominant class
        if cluster_count:
            dominant_class = max(cluster_count, key=cluster_count.get)
            count_in_cluster = cluster_count[dominant_class]
            total_in_class = total_class_count[dominant_class]


            # Calculating the homogenity for each cluster
            if total_in_class > 0:
                completeness = count_in_cluster / total_in_class
            else:
                completeness = 0
        else:
            completeness = 0

        clist.append(completeness)

    return clist

if __name__=="__main__" :

    pos_reviews, neg_reviews = create_docs(10,10)

    positive_docs = create_easy_documents(pos_reviews, 'pos',
                                 filters=[],
                                 transforms=[])

    negative_docs = create_easy_documents(neg_reviews, 'neg',
                                    filters=[],
                                 transforms=[])


    # print("Positive Documents:")
    # for doc in positive_docs:
    #     print(doc.tokens)
    #
    # print("\nNegative Documents:")
    # for doc in negative_docs:
    #     print(doc.tokens)

    # Testing filters and transforms directly
    sample_tokens = ["a", "the", "dog!", "cat", "fish..."]

    # Apply filters
    filtered_tokens = [token for token in sample_tokens if not_stopword(token)]
    print("\nFiltered Tokens (not stopwords):", filtered_tokens)

    # Apply transforms
    transformed_tokens = [remove_trailing_punct(convert_to_lowercase(token)) for token in sample_tokens]
    print("Transformed Tokens (lowercase and no trailing punctuation):", transformed_tokens)





