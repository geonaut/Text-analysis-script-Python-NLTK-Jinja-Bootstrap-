# Text Analyser Script

A short Python project for analysing text files, in order to find the most frequent words. The results are passed to a HTML table, and displayed using Bootstrap and a Jinja2 template. The script uses the natural language processing toolkit (NLTK), to remove 'stopwords', such as common prepositions and pronouns. The script can be passed arguments, to modify the output e.g. only show words that occur more than *x* times. See the Usage section for more information. 

![text_analyser_screenshot](https://github.com/geonaut/Text-analysis-script-Python-NLTK-Jinja-Bootstrap-/blob/master/screenshot.png "screenshot")

## Installation

Written for Python 2.7. 

Modules:

* NLTK
* Jinja2

```bash
sudo pip install nltk jinja2
```

You might need to install some NLTK resources:

* 'punkt' from NLTK
* 'averaged_perceptron_tagger' from NLTK
* 'stopwords' from NLTK

There are commented out download commands at the top of the python file, or you can do this directly from within Python e.g. 

```bash
python
>>>import nltk
>>>nltk.download('punkt')
```
If you have virtualenv installed, you could setup a local virtualenv folder and clone the repo, with the following:

```bash
virtualenv text_analyser
source text_analyser/bin/activate
cd text_analyser
git init .
git remote add origin <this_repo>
git pull origin master
```

## Usage

Run the script from terminal, e.g.

```bash
python text_analyser.py -d test_docs/ -o 5 -l 6
python text_analyser.py -f test_docs/doc3.txt -s 2
```

```bash
usage: text_analyser.py [-h] (-d DIR | -f FILE) [-o OCCURRENCE] [-l LENGTH]
                        [-s SENTENCES]

Text analysis tool for identifying common words and displaying them in a
table, along with context

optional arguments:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     Folder to be analysed
  -f FILE, --file FILE  File to be analysed
  -o OCCURRENCE, --occurrence OCCURRENCE
                        Minimum word occurrence (INT)
  -l LENGTH, --length LENGTH
                        Minimum word length (INT)
  -s SENTENCES, --sentences SENTENCES
                        Number of sentences to display in the context column
                        (INT)
```

## Future ideas

* Use stemming to group similar words. e.g. American & America
* Remove plurals e.g. American & Americans
* Setup 'part of speech' tagging to extract certain types of words, such as verbs or nouns
* Setup input for different files types, including scraped data
* Have one context sentence per file
* Sort the table by word frequency
* Display the word frequency after repsective filenames.

