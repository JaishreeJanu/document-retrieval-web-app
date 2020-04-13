# coding: utf-8
import os
import glob
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from collections import defaultdict
import csv
import json
from operator import itemgetter

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()

data_path = os.getcwd() + '/search_app/index/'

class Inverted():

    def readfile(path, filename):
        '''
        Reads file given in parameter name "filename".
        Parameters:
            path (str) : Path where file is present
            filename : File to be read
        Returns read file in string type
        '''
        with open(path + filename) as file:
            file_as_list = file.readlines()
            file_as_string = ''.join(map(str, file_as_list))

        return file_as_string

    def preprocess(text):
        '''
        Convert text file into normalized tokens
        Parameters:
            text (str) : text to be preprocessed
        
        Returns:
            stemmed (str) : Preprocessed text
        '''
        stemmed = []
        text = text.lower()
        text = re.sub(r'\b[0-9]+\b', '', text) # Removes terms containing only numbers
        tokens = word_tokenize(text) #divides string into lists of substrings
        text_list = [i for i in tokens if not i in stop_words] # Removing stopwords
        for word in text_list:
            word = re.sub(r'[^\w\s]','',word) #Removes punctuation characters (except underscore)
            word = re.sub(r'\_','',word)
            #stemmed_word = (stemmer.stem(word)) #It takes out the root of the word
            stemmed_word = wordnet_lemmatizer.lemmatize(word)
            stemmed.append(stemmed_word)
        return stemmed


    def create_index(terms, docID):
        '''
        Creates Inverted Index in Data structure called dictionary and then save it into a json file.
        Term is index and list of lists is stored as values. Each list item in list is combination of docID and frequency of term in docID.
        Parameters:
            text (str) : text to be indexed in dictionary
            docID (str) : Document Name
        '''
        with open(data_path+'dict.json', 'r') as index:
            ivdict = json.loads(index.read())
        for term in terms:
            if term in ivdict:
                postings_list = [list[0] for list in ivdict[term]]
                if docID in postings_list:
                    ivdict[term][docID-1][1] += 1
                else:
                    ivdict[term].append([docID,1])         
            else:
                ivdict.update({term : [[docID,1]] })
        
        index_file = open(data_path+"dict.json","w")
        index_file.write(json.dumps(ivdict))
        index_file.close()
        return

    def search(query):
        '''
        Returns list of documents containing the terms present in query
        
        Parameters:
            query (str) : Query received from form input
        Returns:
            A list of documents containing query terms
        '''
        #query_list = list(query.split(" "))
        query_list = query
        result = []
        with open(data_path+"dict.json","rb") as iv:
            ivdict = json.load(iv)
        for query in query_list:
            if query in ivdict:
                this_list = ivdict[query]
                this_list = sorted(this_list,key=itemgetter(1), reverse=True)
                this_list = this_list[0:5]
                doc_list = [list[0] for list in this_list]
                for list_item in doc_list:
                    if list_item not in result:
                        result.append(list_item)
        
        return result


