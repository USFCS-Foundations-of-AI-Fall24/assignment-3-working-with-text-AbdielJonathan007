import random
#Abd
from Cluster import *
from Document import *
from make_dataset import create_docs


def classify(clusters, item) :
    dist = 10000
    best = None
    for c in clusters :
        d = cosine_similarity(c.centroid, item)
        if d < dist :
            dist = d
            best = c
    return best.centroid.true_class if best else None

# Used chatgpt as a reference for this method
def five_fold_cross_validation(nwords, nelements) :
    ## generate nelements documents of each type (pos and neg), with nwords words in each doc.
    pos_docs, neg_docs = create_docs(nelements,nwords)
    documents = [{'tokens': doc, 'true_class': 'pos'} for doc in pos_docs] + \
                [{'tokens': doc, 'true_class': 'neg'} for doc in neg_docs]

    random.shuffle(documents)

    # divide the documents into 5 folds.
    folds = [documents[i::5] for i in range(5)]
    accuracies = []

    ## for i = 1 to 5
    for i in range(5):
        test_set = folds[i]
        training_set = [doc for j in range(5) if j != i for doc in folds[j]]

        training_documents = []
        for doc in training_set:
            document = Document()
            document.add_tokens(doc['tokens'])  # Add tokens to the document
            training_documents.append(document)  # Append fully initialized document

        clusters = k_means(2,['pos', 'neg'], training_documents)

        #    use classify to classify the other 20%.
        #    measure accuracy - how many of the documents were classified correctly?
        correct_count = 0
        for test_doc in test_set:
            test_document = Document()
            test_document.add_tokens(test_doc['tokens'])
            predicted_class = classify(clusters, test_document)
            if predicted_class == test_doc['true_class']:
                correct_count += 1

        accuracy = correct_count / len(test_set) if test_set else 0
        accuracies.append(accuracy)

    return sum(accuracies)/ len(accuracies)

def main():
    nwords = 100  # Number of words in each document
    nelements = 10  # Number of documents of each type
    average_accuracy = five_fold_cross_validation(nwords, nelements)
    print(f"Average accuracy over 5 folds: {average_accuracy:.2f}")

if __name__ == "__main__":
    main()



