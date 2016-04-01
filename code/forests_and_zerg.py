# coding: utf-8
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/scrape_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
labels[:10]
soup[:100]
string[:100]
string
import re
my_titles = re.compile("""');">*</a>""").match(str(string))
my_titles = re.compile("""');">*</a>""").match(str(string))
my_delim = """');">*</a>"""
my_delim
my_titles = re.compile(my_delim).match(str(string))
my_titles = re.compile(my_delim)
string.split(""");">""")
string.split(u');">')
my_string = """');""""
my_string = """ ');" """
my_string
my_string[0]
my_string.strip()
my_string = my_string.strip()
string.split(my_string)
str(soup).split(my_string)
my_list = str(soup).split(my_string)
my_list[1:-1]
my_regex = re.compile("""n<li><a href="javascript:PlaySound(\'queen/zquwht01.wav',
 '>Acknowledgement 2</a> <a href="queen/zquwht01.wav"><img class="download_arrow" src="../../../../images/download_arrow.gif" title="Download this sound file directly"/></a></li>\n""")
my_regex = re.compile("""n<li><a href="javascript:PlaySound(\'*.wav',
 '>*</a> <a href="*"><img class="download_arrow" src="../../../../images/download_arrow.gif" title="Download this sound file directly"/></a></li>\n""")
http = httplib2.Http()
status, response = http.request(urlpath)

for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
    if link.has_attr('href'):
        print link
for link in BeautifulSoup(requests.get(urlpath).text):
    if link.has_attr('href'):
        print link
for link in BeautifulSoup(requests.get(urlpath).text, parseOnlyThese=SoupStrainer('a'))
    if link.has_attr('href'):
        print link
for link in BeautifulSoup(requests.get(urlpath).text, parseOnlyThese=SoupStrainer('a')):
    if link.has_attr('href'):
        print link
from bs4 import SoupStrainer
for link in BeautifulSoup(requests.get(urlpath).text, parseOnlyThese=SoupStrainer('a')):
    if link.has_attr('href'):
        print link
import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer

http = httplib2.Http()
status, response = http.request(urlpath)

for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
    if link.has_attr('href'):
        print link['href']
for link in soup.findAll('a', href=True, text='TEXT'):
    print link['href']
for link in soup.findAll('a', href=True):
    print link['href']
for link in soup.findAll('a', href=True):
    print link
for link in soup.findAll('a', href=True):
    print link.contents[0]
for link in soup.findAll('a', href=True):
    print link.contents[0].split('>')[1]
for link in soup.findAll('a', href=True):
    print link.contents[0].split('>')[1]
for link in soup.findAll('a', href=True):
    print link.contents[0]
for link in soup.findAll('a', href=True):
    if '<' not in link.contents[0]:
        print link.contents[0]
for link in soup.findAll('a', href=True):
    if '<' not in link.contents[0]:
        print type(link.contents[0])
for link in soup.findAll('a', href=True):
    if '<' not in link.contents[0]:
        print str(link.contents[0])
for link in soup.findAll('a', href=True):
    if '<' not in link.contents[0]:
        if '<' not in str(link.contents[0]):
            print str(link.contents[0])
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/scrape_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/scrape_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/scrape_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/scrape_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/scrape_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/scrape_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/scrape_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/scrape_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/scrape_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/process_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/process_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/process_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/process_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
samples
tup[1] for tup in samples
np.unique([tup[1] for tup in samples])
import numpy as np
np.unique([tup[1] for tup in samples])
identity_feature
annoyed_feature
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/process_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/audio_functions.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/audio_functions.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/audio_functions.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/audio_functions.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
features
samples
features
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/process_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/process_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/process_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
runfile('C:/Users/cferko/Documents/GitHub/eldritch/code/process_audio.py', wdir='C:/Users/cferko/Documents/GitHub/eldritch/code')
features
runfile('C:/Users/cferko/Desktop/pyAudioAnalysis-master/audioFeatureExtraction.py', wdir='C:/Users/cferko/Desktop/pyAudioAnalysis-master')
runfile('C:/Users/cferko/Desktop/pyAudioAnalysis-master/audioFeatureExtraction.py', wdir='C:/Users/cferko/Desktop/pyAudioAnalysis-master')
runfile('C:/Users/cferko/Desktop/pyAudioAnalysis-master/audioFeatureExtraction.py', wdir='C:/Users/cferko/Desktop/pyAudioAnalysis-master')
runfile('C:/Users/cferko/Desktop/pyAudioAnalysis-master/audioFeatureExtraction.py', wdir='C:/Users/cferko/Desktop/pyAudioAnalysis-master')
runfile('C:/Users/cferko/Desktop/pyAudioAnalysis-master/audioFeatureExtraction.py', wdir='C:/Users/cferko/Desktop/pyAudioAnalysis-master')
runfile('C:/Users/cferko/Desktop/pyAudioAnalysis-master/audioFeatureExtraction.py', wdir='C:/Users/cferko/Desktop/pyAudioAnalysis-master')
samples
samples[0][2]
len(samples[0][2])
test = samples[0][2]
test
mtFeatureExtraction(test, 22050, 0.050*22050, 0.025*22050)
stFeatureExtraction(test, 22050, 0.050*22050, 0.025*22050)
stFeatureExtraction(test, 22050, 0.050*22050, 0.025*22050).shape
stFeatureExtraction(test, 22050, 0.050*22050, 0.025*22050).mean(axis=1)
feature_array = []
for sample in samples:
    this_x = sample[2]
    my_vector = stFeatureExtraction(test, 22050, 0.050*22050, 0.025*22050).mean(axis=1)
    feature_array.append(my_vector)
    
feature_array
feature_array.shape()
np.array(feature_array)
np.array(feature_array).shape
feature_array = np.array(feature_array)
import sklearn
from sklearn.ensemble import *
my_forest = sklearn.RandomForestClassifier()
my_forest = RandomForestClassifier()
identity_label
from sklearn.cross_validation import *
cross_val_score(my_forest, feature_array, identity_label)
cross_val_score(my_forest, feature_array, identity_label, cv=2)
my_forest.fit(feature_array, identity_label)
my_forest.score(feature_array, identity_label)
my_forest.predict(feature_array[0])
my_forest.predict(feature_array[2])
my_forest.predict(feature_array[100])
for arr in feature_array:
    print my_forest.predict(arr)
y
identity_label
my_forest.fit(feature_array, annoyed_label)
my_forest.score(feature_array, annoyed_label)
from sklearn.naive_bayes import *
my_bayes = sklearn.GaussianNB()
my_bayes = GaussianNB()
my_bayes.fit(feature_array, identity_label)
my_bayes.score(feature_array, identity_label)
my_bayes.predict(feature_array[0])
my_bayes.predict(feature_array[5])
my_forest.score(feature_array, annoyed_label)
Fs=22050
mft_array = []
for signal in samples:
    this_x = samples[2]
    medium_features = mtFeatureExtraction(this_x, Fs, 1.0, 1.0, 0.05, 0.05)
    mft_array.append(medium_features)
Fs=22050
mft_array = []
for signal in samples:
    this_x = signal[2]
    medium_features = mtFeatureExtraction(this_x, Fs, 1.0, 1.0, 0.05, 0.05)
    mft_array.append(medium_features)
Fs=22050
mft_array = []
for signal in samples:
    this_x = signal[2]
    medium_features = mtFeatureExtraction(this_x, Fs, 1.0*Fs, 1.0*Fs, 0.05*Fs, 0.05*fs)
    mft_array.append(medium_features)
Fs=22050
mft_array = []
for signal in samples:
    this_x = signal[2]
    medium_features = mtFeatureExtraction(this_x, Fs, 1.0*Fs, 1.0*Fs, 0.05*Fs, 0.05*Fs)
    mft_array.append(medium_features)
mft_array
mft_array[0].shape
mft_array[0][0].shape
mft_array[0][1].shape
mft_array[1][1].shape
mft_array[0][0]
mft_array[0][1].shape
mft_array[0][0].shape
X=[]
for signal in samples:
    this_x = signal[2]
    this_vector = stFeatureExtraction(this_x, 22050, 0.05*22050, 0.025*22050)
    means = this_vector.mean(axis=1)
    std = this_vector.std(axis=1)
    X.append(np.concatenate((means, std))
X=[]
for signal in samples:
    this_x = signal[2]
    this_vector = stFeatureExtraction(this_x, 22050, 0.05*22050, 0.025*22050)
    means = this_vector.mean(axis=1)
    std = this_vector.std(axis=1)
    X.append(np.concatenate((means, std)))
X
X[0]
X=np.array(X)
X.shape
my_forest.fit(X, identity_label)
my_forest.score(X, identity_label)
for train_index, test_index in StratifiedKFold(identity_label, n_folds=2):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = identity_label[train_index], identity_label[test_index]
    my_forest.fit(X_train, y_train)
    print my_forest.score(X_train, y_train)
identity_label = np.array(identity_label)
for train_index, test_index in StratifiedKFold(identity_label, n_folds=2):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = identity_label[train_index], identity_label[test_index]
    my_forest.fit(X_train, y_train)
    print my_forest.score(X_train, y_train)
identity_label = np.array(identity_label)
for train_index, test_index in StratifiedKFold(identity_label, n_folds=2):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = identity_label[train_index], identity_label[test_index]
    my_forest.fit(X_train, y_train)
    print my_forest.score(X_test, y_test)
my_forest = RandomForestClassifier(n_estimators=100)
identity_label = np.array(identity_label)
for train_index, test_index in StratifiedKFold(identity_label, n_folds=2):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = identity_label[train_index], identity_label[test_index]
    my_forest.fit(X_train, y_train)
    print my_forest.score(X_test, y_test)
my_forest = RandomForestClassifier(n_estimators=500)
identity_label = np.array(identity_label)
for train_index, test_index in StratifiedKFold(identity_label, n_folds=2):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = identity_label[train_index], identity_label[test_index]
    my_forest.fit(X_train, y_train)
    print my_forest.score(X_test, y_test)
my_forest = RandomForestClassifier(n_estimators=500)
identity_label = np.array(identity_label)
for train_index, test_index in StratifiedKFold(identity_label, n_folds=3):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = identity_label[train_index], identity_label[test_index]
    my_forest.fit(X_train, y_train)
    print my_forest.score(X_test, y_test)
X.shape
154/2
my_forest = RandomForestClassifier(n_estimators=500)
identity_label = np.array(identity_label)
for train_index, test_index in StratifiedKFold(identity_label, n_folds=3):
    X_train, X_test = X[train_index][:, :77], X[test_index][:, :77]
    y_train, y_test = identity_label[train_index], identity_label[test_index]
    my_forest.fit(X_train, y_train)
    print my_forest.score(X_test, y_test)
my_forest.fit(X, identity_label)
identity_label
importances = forest.feature_importances_
importances = my_forest.feature_importances_
importances
import matplotlib.pyplot as plt
plt.bar(importances)
import seaborn as sns
import seaborn as sns
sns.barplot(importances)
importances
x = range(len(importances))
sns.barplot(x, importances)
sns.barplot(range(1, len(importances)+1), importances)
sns.set_context("poster")
sns.barplot(range(1, len(importances)+1), importances)
sns.set_context("notebook")
get_ipython().magic(u'save forests_and_zerg')
get_ipython().magic(u'save forests_and_zerg 1-172')
