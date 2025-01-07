# PLSA (Probabilistic Latent Semantic Analysis) 

This is a python implementation of Probabilistic Latent Semantic Analysis using EM algorithm.

Support both English and Hindi.

# Usage

Execute the following command in the cmd :

```
python plsa.py [datasetFilePath] [stopwordsFilePath] [K] [maxIteration] [threshold] [topicWordsNum] [docTopicDisFilePath] [topicWordDisFilePath] [dictionaryFilePath] [topicsFilePath]
```

eg. 

```
python plsa.py dataset.txt stopwords.dic 10 30 1.0 10 doctopic.txt topicword.txt dictionary.dic topics.txt 
```

or omit the params using default values specified in plsa.py :

```
python plsa.py
```

The meaning of params are given as following:

|param|description|
|:---:|:---------:|
|datasetFilePath|the file path of dataset|
|stopwordsFilePath|the file path of stopwords|
|K|the number of topic|
|maxIteration|the max number of iteration of EM algorithm|
|threshold|the threshold to judge the convergence of log likelihood|
|topicWordsNum|the number of top words of each topic|
|docTopicDisFilePath|the file path to output document-topic distribution|
|topicWordDistribution|the file path to output topic-word distribution|
|dictionaryFilePath|the file path to output dictionary|
|topicsFilePath|the file path to output top words of each topic|

# Format of inputs

In the dataset file, each line represents a document.

In the stopwords file, each line represents a stopword.

# Samples

## Dataset 1(English)

The dataset is multiple documents in one piece from Wikipedia.

The result of top words is given as :

![sample1](https://github.com/laserwave/PLSA/blob/master/images/sample1.png)

The params are set as :

```
python plsa.py dataset1.txt stopwords.dic 10 20 1.0 10 doctopic.txt topicword.txt dictionary.dic topics.txt 
```

## Dataset 2(English)

The second dataset is 100 documents from the Associated Press.

The result of top words is given as :

![sample2](https://github.com/laserwave/PLSA/blob/master/images/sample2.png)

The params are set as :

```
python plsa.py dataset2.txt stopwords.dic 10 20 50.0 10 doctopic.txt topicword.txt dictionary.dic topics.txt 
```

## Dataset 3(Chinese)

The third dataset is 50 documents from sina.

The result of top words is given as :

![sample3](https://github.com/laserwave/PLSA/blob/master/images/sample3.png)

The params are set as :

```
python plsa.py primates.txt stopwords.dic 30 30 10.0 10 doctopic.txt topicword.txt dictionary.dic topics.txt 
```
