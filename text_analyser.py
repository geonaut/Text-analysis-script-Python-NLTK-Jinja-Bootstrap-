import re
import collections
import nltk
import glob
import os
import argparse
import jinja2
from nltk.corpus import stopwords
from bs4 import BeautifulSoup as Soup
from nltk.tokenize import sent_tokenize, word_tokenize,RegexpTokenizer
import unicodedata

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

parser = argparse.ArgumentParser(description='Text analysis tool for identifying common words and displaying them in a table, along with context')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-d','--dir', help='Folder to be analysed', required=False)
group.add_argument('-f','--file', help='File to be analysed', required=False)
parser.add_argument('-o','--occurrence', type=int, default=5, help='Minimum word occurrence (INT)', required=False)
parser.add_argument('-l','--length', type=int, default=4, help='Minimum word length (INT)', required=False)
parser.add_argument('-s','--sentences', type=int, default=3, help='Number of sentences to display in the context column (INT)', required=False)
args = vars(parser.parse_args())

count = args['occurrence']
length = args['length']
path = args['dir']
sentences = args['sentences']
file = args['file']

def getFileList():
    files = []
    if args['file']:
        files.append(args['file'])
    if args['dir']:
        path = args['dir']
        files = glob.glob(os.path.join(path, '*.txt'))
    return files

def filterText(files,count,length):
    word_list = []
    s=set(stopwords.words('English'))
    for file in files:
        with open(file) as f:
            text = f.read().decode("utf-8")
        #remove stopwords
        filtered = filter(lambda w: not w in s,text.split())
        #word freqency
        counts = collections.Counter(filtered)
        #remove infrequent words
        frequentWords = [k for k, v in counts.iteritems() if v > count]
        #remove alphanumeric
        tokenizer = RegexpTokenizer(r'\w+')
        alphaonly = tokenizer.tokenize(str(frequentWords))
        #remove words shorter than n letters
        y = [s for s in alphaonly if len(s) > length]
        word_list.extend(y)
    return set(word_list)

word_list = list(filterText(getFileList(),count,length))

def getContainingFiles(word,files):
    filenames = []
    for filename in files:
        with open(filename) as f:
            text = f.read().decode("utf-8")
            if word in text:
                filenames.append(filename)
    return filenames

def getSentenceList(word,files,sentences):
    s = sentences
    sentence_list = []
    for filename in files:
        with open(filename) as f:
            text = f.read().decode("utf-8")
            sentences = (sent_tokenize(text))
            for sentence in sentences:
                if word in sentence:
                    sentence = unicodedata.normalize('NFKD', sentence).encode('ascii','ignore')
                    toreplace = "<b>\g<0></b>"
                    pattern = re.compile(re.escape(word), re.I)
                    highlightedSentence = (re.sub(pattern,toreplace,sentence))
                    sentence_list.append(highlightedSentence)
    return sentence_list[0:s]

def assembleOutput(word_list,sentences):
    items = []
    for word in word_list:
        files = getFileList()
        documentList = getContainingFiles(word,files)
        sentenceList = getSentenceList(word,files,sentences)
        item = dict(word = word,documents = documentList,sentences = sentenceList)
        items.append(item)
    return items

loader = jinja2.FileSystemLoader('table_template.html')
env = jinja2.Environment(loader=loader)
template = env.get_template('')
output = template.render(items=assembleOutput(word_list,sentences))

Html_file= open("output.html","w")
Html_file.write(str(output))
Html_file.close()







