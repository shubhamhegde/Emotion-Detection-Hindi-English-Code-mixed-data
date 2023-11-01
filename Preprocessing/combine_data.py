import json 
import pandas as pd
import re
import string
from sklearn.model_selection import train_test_split


# tweet_sentence_data_path = "./data/tweet_data.json"
# tweet_label_data_path = "./data/Towards_Emotion_Recognition_emotions_labelled.csv"

# with open(tweet_sentence_data_path, 'r') as j:
#      data = json.loads(j.read())

# df1 = pd.DataFrame(list(data.items()), columns=['tweet_id', 'tweet'])
# print(df1.head())
# print(len(df1))
# #Basic Preprocessing
# def cleanSentence(sentence):
#   sentence = sentence.lower()
#   sentence = sentence.rstrip().replace("\n"," ").replace("\r"," ")
#   sentence = re.sub(' +', ' ', sentence)
#   sentence = sentence.translate(str.maketrans('', '', string.punctuation))
#   return sentence

# df1["tweet"]= df1['tweet'].apply(lambda x : cleanSentence(x))

# # print(df1.dtypes)

# df2 = pd.read_csv(tweet_label_data_path,  dtype={'tweet_id': object})
# print(df2.head())
# print(len(df2))
# # print(df2.dtypes)



# df3 = df1.merge(df2, on='tweet_id', how='inner')
# print(df3.head())
# print(len(df3))

# print(df3.shape)

# df3.to_csv("./data/Towards_Emotion_Recognition_text&emotions.csv",index=False)



df3 = pd.read_csv("./data/Towards_Emotion_Recognition_text&emotions.csv")
print(df3.head())


train, test = train_test_split(df3, test_size=0.2)

train = train.reset_index(drop=True)
test = test.reset_index(drop=True)

print(len(train),len(test),len(df3))

train.to_csv("./data/TER_text&emotions_train.csv",index=False)
test.to_csv("./data/TER_text&emotions_test.csv",index=False)
