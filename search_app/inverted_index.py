# coding: utf-8
import os
import glob
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
from nltk.stem import PorterStemmer
from collections import defaultdict
import csv
import json
from operator import itemgetter

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

#path = os.getcwd() + '/documents/'
data_path = os.getcwd() + '/search_app/index/'
#files = os.listdir(path)
ivdict = {}

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
        Preprocesses text.
        Parameters:
            text (str) : text to preprocessed
        
        Returns:
            stemmed (str) : Preprocessed text
        '''
        stemmed = []
        text = text.lower()
        text = re.sub(r'\d+', '', text)
        text = re.sub(r'[^\w\s]','',text)
        tokens = word_tokenize(text)
        text_list = [i for i in tokens if not i in stop_words]
        for word in text_list:
            stemmed_word = (stemmer.stem(word))
            stemmed.append(stemmed_word)
        return stemmed


    def create_index(text,docID):
        '''
        Creates Inverted Index in Data structure called dictionary and then save it into a json file.
        Term is index and list of lists is stored as values. Each list item in list is combination of docID and frequency of term in docID.
        Parameters:
            text (str) : text to be indexed in dictionary
            docID (str) : Document Name
        '''
        for term in text:
            if term in ivdict:
                flag=0
                for i in range(len(ivdict[term])):
                    if ivdict[term][i][0] == docID:
                        ivdict[term][i][1] += 1
                        flag=1
                        break;
                if flag == 0:
                    ivdict[term].append([docID,1])
            else:
                myList = [[docID,1]]
                ivdict.update({term : myList })
        
        js = json.dumps(ivdict)
        iv = open(data_path+"dict.json","w")
        iv.write(js)
        iv.close()
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


