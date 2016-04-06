import pandas as pd
import nltk
from nltk.corpus import brown
from nltk.tokenize import RegexpTokenizer

from nltk.corpus import PlaintextCorpusReader

def get_names():
    f = open("warforged_names.txt")
    forgeling_names = f.read()
    forgeling_names = forgeling_names.replace("\n", "\t").split("\t")
    f.close()
    
    name_frame = pd.read_csv("names_df.csv")
    human_names = list(name_frame[name_frame["Race"]=="Human"]["Name"].values)
    
    f2 = open("extra_human_names.txt")
    more_names = f2.read()
    more_names = more_names.replace("\n", " ").replace(r"\x"," ").split(" ")
    more_names = filter(lambda x: len(x)>1 , more_names)
    more_names.remove('S\xe9verin') ## Hack, can't figure out how to remove this
    more_names += ['Severin']
    f2.close()
    
    human_names += more_names
    
    return forgeling_names, human_names

def train_function(feature_function):
    global human_names, forgeling_names
    
    train_x = human_names[:200] + forgeling_names[:200]
    train_y = ["Human"]*200 + ["Forgeling"]*200
    
    test_x = human_names[200:] + forgeling_names[200:]
    test_y = ["Human"]*(len(human_names)-200) + ["Forgeling"]*(len(forgeling_names)-200)
    
    train_set = [ (feature_function(name), train_y[index] ) 
                for index, name in enumerate(train_x)]
                    
    test_set = [ (feature_function(name), test_y[index] ) 
                for index, name in enumerate(test_x)]
                    
    classifier = nltk.DecisionTreeClassifier.train(train_set)
    accuracy = nltk.classify.accuracy(classifier, test_set)
    
    return classifier, accuracy
    
forgeling_names, human_names = get_names()

def process_element(element):
    element = element.replace(u"\u2019", "'")
    element = element.replace(u"\u2018", "'")
    element = element.replace(u"\u2014", " ")
    element = element.lower()
    
    return element

def process_nan():
    corpus_root = '../nan_samples/'
    library = PlaintextCorpusReader(corpus_root, '.*', encoding='utf-8')
    tokens = nltk.word_tokenize(library.raw())
    tokens = map(lambda x: process_element(x), tokens)
    nan_tokens=[]
    for i in tokens:
        nan_tokens+=i.split(' ')
    return nan_tokens

def process_brown():    
    tokenizer = RegexpTokenizer(r'\w+')
    brown_toks = tokenizer.tokenize(brown.raw()[:50000])
    brown_toks = list(set(brown_toks))
    brown_toks= map(lambda x: x.lower(), brown_toks)
 
    return brown_toks
    
def score_language(feature_function):
    nan_toks = process_nan()
    brown_toks = process_brown()
    
    train_x = nan_toks[:400] + brown_toks[:800]
    train_y = ["Nan"]*400 + ["Human"]*800
    
    test_x = nan_toks[400:] + brown_toks[800:]
    test_y = ["Nan"]*(len(nan_toks)-400) + ["Human"]*(len(brown_toks)-800)
    
    train_set = [ (feature_function(name), train_y[index] ) 
                for index, name in enumerate(train_x)]
                    
    test_set = [ (feature_function(name), test_y[index] ) 
                for index, name in enumerate(test_x)]
                    
    classifier = nltk.DecisionTreeClassifier.train(train_set)
    accuracy = nltk.classify.accuracy(classifier, test_set)
    
    return classifier, accuracy
    
forgeling_names, human_names = get_names()