# Topic modeling and recommender system of fairy tales

## Objective
This project aims to identify topics in fairy tales, compare the topics between different continents, and develop a recommender system for fairy tales.


## Findings
- Using the LDA model, 8 topics are identified from the fairy tales: poor vs. rich (24.4%), humans&animals (18.2%), animal characters (17.7%), love (15.8%), holiday (13.5%), nature (4.6%), farm (3.2%), and family (2.5%). 
- Across different continents, human&animals is a prevalent popular topic. It is one of the top 3 topics for every continent. Poor vs. rich is prevalent in all the continents except in Oceania, and animal characters are relatively more common in all the continents except in North America. Holiday topic is more popular in Asia and North America.

## Methodology

### Data Collection
Over 3000 fairy tales are scraped from https://fairytalez.com/. The fairy tales are from all over the world, including 6 continents: Africa, Asia, Europe, South America, North America and Oceania. The region and author/editor/collector of each fairy tale are also scraped from website. 


### Data preprocessing
The fairy tales are cleaned primarily using spaCy and regex. The comprehension questions and notes in fairy tales are identified by regex removed first. Then numbers, punctuations and stop words are removed from the text. All the words are converted to lower case and lemmatized afterwards.  
After lemmatization, all the fairy tales are converted into a document-term matrix using TF-IDF. The argument min_df is set to 3 to remove the rare words in the text (e.g. words from other languages). Unigram, bigram and trigram are all used for topic modeling.




### Models
- LSA
- LDA


### Technologies
- pandas
- numpy
- sklearn
- seaborn
- matplotlib
- re
- Beautiful Soup
- nltk
- pickle
- spaCy
- gensim
- Flask
- html/css
- Tableau
- Heroku
- Google Cloud Platform

## Deliverables (data files are not included)
- Jupyter notebooks for:
  - Web scrapping
  - Text preprocessing and topic modeling
  - Tableau visualizations
  - Recommender system and other visualizations
- Folder for web app (https://fairytales-recommender1128.herokuapp.com/)
- Folder for Tableau Dashboard and Excel documents
- Presentation deck
- Video for recommender system app demo used in presentation