### Assignment 3: Working with text
#### Due Mon Oct 7, 11:59pm

Note: For the programming  portions of the assignment, please provide a file called submission.py that demos your code.
For the written portions, please prepare a document called assignment3.pdf and put your answers in there.
And don't forget to put your name on your assignment!

**On time management!** This assignment has many small components; the key to success will be starting early.
I've added suggested milestones _in italics_. 

**Problem 1. Pandas.** _(Sept 30)_

This problem will give you some experience working with Pandas. In assignment 4 we'll use Pandas to process data for learning.

Please add a file called pandasExercise.py to your repo containing this part.

First, read through [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html). There's a ton of other useful documentation of the pandas site as well.

The rest of these exercises use [The Pandas Cookbook](https://github.com/PacktPublishing/Pandas-Cookbook). We'll also use the breast cancer dataset included in the GitHub repo. This is a classic ML dataset originally from the UCI ML data repositoryLinks to an external site..
The Pandas cookbook itself is here: [https://www.packtpub.com/en-us/product/pandas-cookbook-9781784393878](https://www.packtpub.com/en-us/product/pandas-cookbook-9781784393878) - use your USFConnect credentials to log in. 

**(5 points)** read Chapter 1. Then, write a function that will read in the breast cancer dataset and print out the classification column, which is the left-most column.

**(5 points)** read Chapter 2. Then, write a function that computes ZeroR (the most common classification) for the breast cancer data. (either 'recurrence-events' or 'no-recurrence-events')

**(5 points)** read Chapter 3. Then write a function that determines the most common value for age and menopause for patients with recurrences.

**(5 points)** Read Chapter 4. Write a function that plots the number of recurrences for each age group.

**Problem 2: Documents** 

In the rest of this assignment, we'll build some tools 
to allow us to classify and cluster text. We'll deliberately keep it pretty simple to
allow us to understand what's going on. 

To begin, consider the Document class. This represents a text document. It has two member variables: 
true_class, which represents the class it belongs to, and tokens, which represents the tokens comprising 
the document. Tokens is a defaultdict - if we access a key that is not present, it will create a key mapping to
the value 0.

I've provided the beginnings of a test harness for you in test_Document.py.

**(10 points) _Sept 25_ I've implemented euclidean_distance, along with a basic test, and a test for cosine_similarity.
Implement cosine similarity. Use your test to ensure that it works.**

We need some better documents. For now, we're going to control our lexicon tightly to let us focus on
the algorithms. In the next assignment, we'll deal with more complex data.

make_dataset.py will generate random sequences of tokens for us from a controlled list of words. Here we have two
classes, pos and neg. 
In Loader.py, I've also provided a function called create_easy_documents that will take in a list of lists of tokens and return
a list of Document objects. You can see how these work in the main.

There's also an accompanying test_Loader.py. One of the tests in there is test_workflow. As you're assembling
the pieces of this, you will find it helpful to have a tester to let you try things out.

2. Now we're ready to work on Cluster.py. A Cluster is a list of documents (stored in self.members) and a centroid, stored in self.centroid.
The centroid is also a Document whose token counts are the *average* of all the token counts of its members.
   (if we think of the documents as vectors or points, the centroid is the mean of those points)

**(10 points) _(Sept 26)_ You complete calculate_centroid. It should create a new Document whose members are the tokens of all its members, with the count averaged.**

**Also complete the unit test in test_Cluster.py and convince yourself that it works.** 

3. Once we can compute centroids, we're ready to implement k-means. The stub is in Cluster.py. 

**(10 points) _(Sept 30)_ Fill in the rest of the algorithm. 
I've given you the beginnings of a unit test in test_Cluster.py. Extend it to use the document generator we built before.**

4. Now we need to evaluate performance. Two ways to measure clustering are homogeneity and completeness. _Homogeneity_ 
is the fraction of samples in a cluster that are the largest class. So if our cluster is ['pos','pos','neg','pos'], homogeneity is 0.75. 
(Note that in this case homogeneity is the same as accuracy.) _Completeness_ is the fraction of articles from a class that are in the same cluster.
So if we had c1 = ['pos','neg','pos'] and c2 = ['pos','neg',neg'] then both c1 and c2 would have a completeness score of 0.66, as
they each contain 2/3 of the samples from their dominant class.

**(10 points) _(Oct 2)_ Complete compute_homogeneity and compute_completeness, implement unit tests for each of them,
and then add them to your workflow unit test.**

5. Your clusterer should work pretty well on this data. The lexicons are pretty small, and quite
different from each other. Let's make it harder.

Return to make_dataset.py. Extend pos_lexicon and neg_lexicon to 25, 50, 100, 500, and 1000 random words each.
(you can use ollama to generate these.)

**(5 points) _(Oct 3)_ Re-run your clusterer with each of these different lexicons. Prepare a table showing your results and include it in your answer doc.**

As the number of tokens grows, clustering algorithms struggle with the _curse of dimensionality_. This is a core challenge in
machine learning. In later assignments, we'll see how to use _embeddings_ to deal with this. 

6. Our data is also pretty clean looking. Let's mess it up.

**(10 points) _(Oct 5)_ Modify make_dataset so that with p=0.3, a random punctuation character (from string.punctuation) is added to a word, 
and with p=0.2 the word becomes capitalized (i.e. cat becomes Cat). Both results can occur to the same word.** 

Real-world text also contains a lot of words that are not helpful for categorizing documents, such as a,an,he,she, 
is, was, their, across, and many more. We call these 'stopwords'.

**(5 points) _(Oct 5)_ Modify make_dataset so that with p=0.2, rather than selecting a word from the lexicon, it selects one of
['a','an', 'the']**

**Rerun your clusterer with 100 random words per document and these new additions. Add a line to your answer doc indicating the performance.**

7. Cleaning and preprocessing your data is a really important part of working with text. We'll do a few simple things here,
and also see again how we can use Python's concept of functions as objects to preserve flexibility.

There are two aspects to this process: filtering and transforming. 

Filtering removes tokens that we don't want.

**(5 points) _(Oct 7)_ I've provided a sample filter, called not_cat. You implement not_stopword. It should return true if
the token is not ['a','an', 'the']. You can see where filters are applied in create_easy_documents.**

Transforming changes the token. 

**(5 points) _(Oct 7)_ Implement the two transforms in Loader.py: remove_trailing_punct and 
convert_to_lowercase. (Undoing the messiness we introduced above.) Add unit tests for each of these in test_Loader.py.
Once they're working, extend create_easy_documents to apply the transforms to each token. 
Re-run your workflow now that you've added this new functionality. You should have the same performance as before we 
messed up our data.** 

8. We can also use this clustering approach to create a _classifier_. Once we've built our clusters,
we can look at new documents and label them according to the cluster they're closest to. I've provided a 
function in Classifier called classify. It takes a list of clusters and an item and returns the class it predicts the
item belongs to.

In order to evaluate our classifier's effectiveness, we want to create a training set and a test set. In order to
avoid bias, we'll use five-fold cross-validation.

**(10 points) _(Oct 9)_ Complete the five-fold cross-validation function in Classifier.py. Add a main to this file that allows a user to run your
program from the command line.** 

