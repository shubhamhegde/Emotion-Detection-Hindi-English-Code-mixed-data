# Emotion-Detection-Hindi-English-Code-mixed-data

## Dataset :

Towards-Emotion-Recognition https://github.com/anshulwadhawan/emotion_detection

hinglishNorm https://github.com/piyushmakhija5/hinglishNorm

Subword-LSTM https://github.com/drimpossible/Sub-word-LSTM

code_mix_sentences_emotions_tagged https://linguisticresources.weebly.com/downloads.html

Our dataset comprises of around 140k
tweets labelled with six standard human emotions
- disgust, anger, happiness, sadness, surprise and
fear.

## Introduction
With growth in communication over social media
like Twitter and Facebook, huge amounts of natural
language data is available that can be leveraged to
create useful applications. Emotion detection is
one such popular application that has been widely
researched. Emotion detection helps in social media monitoring, product analysis, market research,
customer satisfaction analysis, etc. A lot of work
has been done in sentiment analysis of monolingual data as enormous amounts of labelled data is
available for this. However, emotion detection for
multilingual data is still a largely unexplored space.
Multilingual data in social media is a norm.
One such widely used language in social media
is Hinglish - a hybrid of English and Hindi. According to census 2011, 43.63% population of India speak Hindi and a detailed analysis of Hindi-English bilingual users on Facebook showed that
17.2% of all posts ,which accounted for around
one-fourth of the words in their dataset revealed
some form of code-mixing(Bali et al., 2014) Dealing with code-mixed data in itself is challenging
due to lack of well annotated data, ambiguities in
spellings, no grammar rules, abbreviations, etc.
Our project is an attempt to to assemble an annotated dataset for this, represent them appropriately
with embeddings for code-mixed data, and further
detect emotion from such bilingual Hindi-English
(Hinglish) code-switched texts. We have collected
and compiled a dataset of code-mixed tweets with
labelled emotions. After pre-processing and codemix normalization, we generated word embeddings
using FastText(Bojanowski et al., 2016). We experimented with multiple models to predict the emotion
results showed that Attention based Bi-directional
LSTM performed the best with 86% accuracy.

## Pre-processing
To clean the dataset and use it in the model pipeline,
multiple pre-processing steps were applied.
Since the collected data was essentially tweets, first
tweet-specific cleaning was required. This included
removal of hashtags, URLs and other special characters like emojis. We then converted the text to
lowercase and restricted the tweet length to avoid
longer length texts.
Code-mix specific preprocessing was an integral
part of our work. While dealing with tweets, normalizing them , i.e, converting misspelt and abbreviated words to a standardized form is a a necessity.
Though there has been previous work in normalizing English tweets (Gupta and Joshi, 2017), there
is limited research done on code-mixed data. We
performed code-mix normalization in a rule-based
fashion. An initial exploratory analysis was done
to understand possible misspellings of frequently
occurring words. On this, a set of rules were applied to translate them to their standardized forms.
Apart from English stopword removal, we also performed code-mixed stop word removal. As there is
no predefined list of stopwords for such a dataset,
once again, analysis of most frequently occurring
words was used to perform this filtering.

## Embeddings
Before running the Machine Learning models, the
preprocessed corpus has to be converted to embeddings. Word Embeddings are vector representations to encode the meaning of words such that
similar words are closer in distance. Several word
embedding methods are available for monolingual
languages. However Hindi-English code-mixed
pretrained bilingual word embedding is unavailable. Hence, we trained FastText (Bojanowski
et al., 2016) on our corpus to obtain word embeddings for Hinglish.
FastText is a library for learning of word embeddings created by Facebook’s AI Research lab in
2016. FastText is particularly useful as it not only
learns the vector representations for the words
present in the corpus but also has the ability to
learn for Out Of Vocabulary (OOV) words. This
is because FastText learns the weights for the entire word and also for the character n-grams of
the word. Since the same word can have different similar spellings in social media (for example :
chlo, chalo, chaalo), FastText would be the perfect
choice for learning word embeddings for such a
dataset.
We trained FastText on our corpus using the Gensim module which is a fast native C implementation
of FastText with Python interface. It was trained
using negative sampling with a window size of 10
for 10 epochs. This is then used to build the embedding matrix which is used as the input layer for
the various deep learning models outlined in the
following section

## Models

|Models|Accuracies|
|------|------|
|Attention-BiLSTM|86%|
|BiLSTM|83%|
|LSTM|83%|
|CNN|81%|

## Results and Discussion
We experimented with four different methodologies, i.e., CNN, LSTM, BiLSTM and BiLSTM
with Attention. CNN model gave us an accuracy
of 81% on the validation set. We observed that the
validation loss started increasing as the number of
epochs increased. This is a sign of overfitting the
model. We tried LSTM and found the accuracy to
be 83% on the validation set. In this case as well,
we could see an uptick in the validation loss thus
indicating overfitting.
BiLSTM model proved to give us a satisfactory
result with an accuracy of around 83%. We then
added attention mechanism on top of BiLSTM
which increased our accuracy to 86% on the validation set. Both The validation loss training loss
are decreasing. This gave us a better insight into
the tweet data. Compared to the reference paper’s
accuracy of around 72%, our implementation gave
a better performance on the dataset.
