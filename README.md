## SEARCHIT: A web application for information retrieval from document collection

**Motivation**: This application has been inspired by search engines which enable us to retrieve information from large document collection. This application lets you add documents in local folder, take query terms as input and retrieve documents which contain those query terms. It retrieves documents for **conjunctive and disjunctive queries**.

### Technical skills used
- Django web framework
- nltk: Natural language toolkit
- HTML, javascript

### Component 1: Create index

**Inverted index** is created on all documents. Inverted index is a database index storing mapping from words to location or set of documents.
A example of inverted index from my set of documents:

```
{"databas": [["computer.txt", 2], ["bhaskar.txt", 2]], "oper": [["computer.txt", 2]], "system": [["computer.txt", 2], ["yoga.txt", 2]], "comput": [["computer.txt", 2]], "scienc": [["computer.txt", 2]], "program": [["computer.txt", 2]], "languag": [["computer.txt", 2]], "spring": [["computer.txt", 2], ["bhaskar.txt", 2], ["yoga.txt", 16]], "fresh": [["computer.txt", 2], ["bhaskar.txt", 2], ["yoga.txt", 4]], "semest": [["computer.txt", 2]], "bhaskar": [["bhaskar.txt", 2]], "janu": [["bhaskar.txt", 2]], "massag": [["bhaskar.txt", 2], ["yoga.txt", 2]], "digest": [["bhaskar.txt", 2], ["yoga.txt", 2]], "flask": [["bhaskar.txt", 2]], ["name.txt", 1]],  "sunil": [["bhaskar.txt", 2], ["name.txt", 1]], "bikan": [["bhaskar.txt", 2]], "munich": [["bhaskar.txt", 2]], "final": [["yoga.txt", 2]], "like": [["yoga.txt", 2]]
```

For every word, there is list of lists. Each list item stores **document name** and **frequency of term in the document**.


### Component 2: Return search results

- Take the query terms from form, preprocess query and return most relevant document names based on the frequency of the term.

### Development setup

```
cd <project directory>
source virtual_env/bin/activate
python3 manage.py runserver
```
Application server running at : http://localhost:8000/search




