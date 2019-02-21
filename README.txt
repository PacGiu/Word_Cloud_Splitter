This is a word cloud splitter.
In the Study notebook I tested various clustering methods and tree structures.
Once the database is created, it is possible to use "Words_Cloud_Splitter.ipynb " 
as API interface for splitting the word cloud.

The repository contains the following:

NOTEBOOKS: (Python 3)

Topics_Clustering.ipynb - Study of the data and clustering method. Saves a json file with the needed processed data

Words_Cloud_Splitter.ipynb - User-friendly interface test, to validate the method 

SCRIPT:

Cluster.py - Class definition, used in "Words_Cloud_Splitter.ipynb"

DATA:

compact_df.json - Stored processed data, used in "Words_Cloud_Splitter.ipynb"

posts_with_topics.json - Original data, used in "Topics_Clustering.ipynb"