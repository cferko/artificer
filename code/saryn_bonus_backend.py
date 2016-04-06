from nltk.classify import NaiveBayesClassifier
import nltk.sentiment
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.tokenize import regexp
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_objectivity_analyzer():
    n_instances = 100
    subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
    obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]
    
    train_subj_docs = subj_docs
    train_obj_docs = obj_docs
    training_docs = train_subj_docs+train_obj_docs
    sentim_analyzer = SentimentAnalyzer()
    all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])
    
    unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
    
    sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)
    
    training_set = sentim_analyzer.apply_features(training_docs)

    trainer = NaiveBayesClassifier.train
    sentiment_classifier = sentim_analyzer.train(trainer, training_set)
    
    return sentim_analyzer
    
def classify_objectivity(text):
    global _objectivity_analyzer
    
    word_tokenizer = regexp.WhitespaceTokenizer()
    
    tokenized_text = tuple([word.lower() for word in word_tokenizer.tokenize(text)])
    return _objectivity_analyzer.classify(tokenized_text)

def sentiment(text):
    global _objectivity_analyzer
    
    word_tokenizer = regexp.WhitespaceTokenizer()
    
    tokenized_text = tuple([word.lower() for word in word_tokenizer.tokenize(text)])
    objectivity = _objectivity_analyzer.classify(tokenized_text)

    sid = SentimentIntensityAnalyzer()
    pol_scores = sid.polarity_scores(text)
    pol_scores["objectivity"] = objectivity
    
    my_out_dict={}    
    my_out_dict["positivity"] = pol_scores["pos"]
    my_out_dict["negativity"] = pol_scores["neg"]
    my_out_dict["neutrality"] = pol_scores["neu"]
    my_out_dict["compoundness"] = pol_scores["compound"]
    my_out_dict["objectivity"] = pol_scores["objectivity"]

    return my_out_dict
    
if __name__=="__main__":
    _objectivity_analyzer = get_objectivity_analyzer()
    global _objectivity_analayzer