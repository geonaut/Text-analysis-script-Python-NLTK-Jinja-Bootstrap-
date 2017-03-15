# Text Analyser Script

A short Python project for analysing text files, in order to find the most frequent words. The script uses the natural language processing toolkit (NLTK), to remove 'stopwords', such as common prepositions and pronouns. The script can be passed arguments, to modify the output. See the Usage section for more information. 

## Installation

Written for Python 2.7. There are no strict dependencies, but some resources are better downloaded once, outside the script.

* 'punkt' from NLTK
* 'averaged_perceptron_tagger' from NLTK

If you have virtualenv installed, you could setup a local virtualenv folder and clone the repo, following:

```bash
virtualenv text_analyser
source text_analyser/bin/activate
cd text_analyser
git init .
git remote add origin <this_repo>
git pull origin master
```

## Usage

Run the script from terminal:

```bash
python word_counter1.py -d test_docs/ -c 5 -l 6
```

Arguments:

```bash
optional arguments:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     Folder to be analysed
  -f FILE, --file FILE  File to be analysed
  -c COUNT, --count COUNT
                        Minimum word occurrence (INT)
  -l LENGTH, --length LENGTH
                        Minimum word length (INT)
```

## Future ideas

