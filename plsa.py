import os
import streamlit as st
import pandas as pd
import numpy as np
import codecs
import re
from nltk.tokenize import word_tokenize

st.title("Final Project Demo")

# Input for dataset file path
dataname = st.text_input("Type path for dataset (without .txt extension):")
datasetFilePath = f"C://Users//anany//Desktop//college_stuff//SEM7//CS626//{dataname}.txt"
stopwordsFilePath = "C://Users//anany//Desktop//college_stuff//SEM7//CS626//stopwords.dic"

# Define default parameters
K = 10    # Number of topics
topicWordsNum = 10

# File existence check
if dataname:
    if not os.path.exists(datasetFilePath):
        st.error("Please enter a valid dataset file path!")
    elif not os.path.exists(stopwordsFilePath):
        st.error("Stopwords file not found!")
    else:
        # Load and preprocess data
        def preprocessing_plsa(datasetFilePath, stopwordsFilePath):
            # Read the stopwords file
            file = codecs.open(stopwordsFilePath, 'r', 'utf-8')
            stopwords = [line.strip() for line in file]
            file.close()

            # Read the documents
            file = codecs.open(datasetFilePath, 'r', 'utf-8')
            documents = [document.strip() for document in file]
            file.close()

            # Number of documents
            N = len(documents)

            wordCounts = []
            word2id = {}
            id2word = {}
            currentId = 0

            # Generate the word2id and id2word maps
            for document in documents:
                segList = word_tokenize(document)
                wordCount = {}
                for word in segList:
                    word = word.lower().strip()
                    if len(word) > 1 and not re.search('[0-9]', word) and word not in stopwords:
                        if word not in word2id.keys():
                            word2id[word] = currentId
                            id2word[currentId] = word
                            currentId += 1
                        if word in wordCount:
                            wordCount[word] += 1
                        else:
                            wordCount[word] = 1
                wordCounts.append(wordCount)

            # Length of dictionary
            M = len(word2id)

            # Generate the document-word matrix
            X = np.zeros([N, M], dtype=np.int8)
            for word in word2id.keys():
                j = word2id[word]
                for i in range(0, N):
                    if word in wordCounts[i]:
                        X[i, j] = wordCounts[i][word]

            return N, M, word2id, id2word, X

        # Perform preprocessing
        N, M, word2id, id2word, X = preprocessing_plsa(datasetFilePath, stopwordsFilePath)

        # Mock model for demonstration
        theta = np.random.rand(K, M)

        # Extract topics
        def output_diri_test():
            topics = []
            for i in range(0, K):
                topicword = []
                ids = theta[i, :].argsort()  # Get sorted word indices for topic i
                for j in ids:
                    if j < M:  # Ensure j is within the valid range for id2word
                        topicword.insert(0, id2word.get(j, "UNKNOWN"))  # Add "UNKNOWN" if id2word[j] does not exist

                topics.append(topicword[0:min(topicWordsNum, len(topicword))])
            return topics

        topics = output_diri_test()

        # Convert to a DataFrame for better visualization
        df = pd.DataFrame(topics, columns=[f"Word {i+1}" for i in range(topicWordsNum)])
        df.index = [f"Topic {i+1}" for i in range(K)]

        # Display results
        st.write(f"The latent space dimension is {K}")
        st.write("Top Words for Each Topic:")
        st.dataframe(df)
