Probabilistic Latent Semantic Analysis (PLSA)

This is a Python implementation of Probabilistic Latent Semantic Analysis (PLSA) using the Expectation-Maximization (EM) algorithm. The model supports both English and Chinese datasets.

Usage

To execute the PLSA algorithm, run the following command:

python plsa.py [datasetFilePath] [stopwordsFilePath] [K] [maxIteration] [threshold] [topicWordsNum] [docTopicDisFilePath] [topicWordDisFilePath] [dictionaryFilePath] [topicsFilePath]

For example:

python plsa.py dataset.txt stopwords.dic 10 30 1.0 10 doctopic.txt topicword.txt dictionary.dic topics.txt

You can also omit the parameters to use default values specified in plsa.py:

python plsa.py

Parameter Descriptions

| Param                    | Description                                                         |
|--------------------------|---------------------------------------------------------------------|
| datasetFilePath           | Path to the dataset file                                            |
| stopwordsFilePath         | Path to the stopwords file                                          |
| K                         | Number of topics                                                    |
| maxIteration              | Maximum number of iterations for the EM algorithm                   |
| threshold                 | Threshold for convergence based on log likelihood                   |
| topicWordsNum             | Number of top words for each topic                                  |
| docTopicDisFilePath       | Path to output document-topic distribution                          |
| topicWordDisFilePath      | Path to output topic-word distribution                              |
| dictionaryFilePath        | Path to output the dictionary                                        |
| topicsFilePath            | Path to output the top words of each topic                          |

Input Format

- Dataset File: Each line represents a document.
- Stopwords File: Each line contains a stopword.

Sample Datasets

Dataset 1 (English)
This dataset contains 16 documents from Wikipedia about a particular topic.

To run the model:

python plsa.py dataset1.txt stopwords.dic 10 20 1.0 10 doctopic.txt topicword.txt dictionary.dic topics.txt

The result will show the top words for each topic.

Dataset 2 (English)
This dataset contains 100 documents from the Associated Press.

To run the model:

python plsa.py dataset2.txt stopwords.dic 10 20 50.0 10 doctopic.txt topicword.txt dictionary.dic topics.txt

Dataset 3 (Chinese)
This dataset contains 50 documents from Sina.

To run the model:

python plsa.py dataset3.txt stopwords.dic 30 30 10.0 10 doctopic.txt topicword.txt dictionary.dic topics.txt

Output Files

1. Document-Topic Distribution: Distribution of topics for each document.
2. Topic-Word Distribution: Distribution of words for each topic.
3. Dictionary: The vocabulary used in the dataset.
4. Top Words: The top words of each topic.

License

Copyright 2016 ZhikaiZhang

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Author

- Zhikai Zhang  
  Email: zhangzhikai@seu.edu.cn  
  Blog: http://zhikaizhang.cn
