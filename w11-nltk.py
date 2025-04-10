import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string

stop_words = set(stopwords.words('english'))

with open("MAAN_dialog.json","r",encoding="utf-8") as infile:
    play = json.load(infile)
    beatrice_lines = []
    benedick_lines = []
    for line in play:
        if line["role"] == "BEATRICE":
            beatrice_lines.append(line["dialog"])
        elif line["role"] == "BENEDICK":
            benedick_lines.append(line["dialog"])
    beatrice_tokens = word_tokenize(" ".join(beatrice_lines))
    filtered_beatrice_tokens = [w for w in beatrice_tokens if not w.lower() in stop_words and not w.lower() in string.punctuation and not w.lower() in ["’","‘"]]
    beatrice_fdist = FreqDist(filtered_beatrice_tokens)
    # print(beatrice_fdist.most_common(10))
    # print(len(set(filtered_beatrice_tokens))/len(filtered_beatrice_tokens))
    beatrice_nnps = []
    for i in nltk.pos_tag(filtered_beatrice_tokens):
        if i[1]=="NNP":
            beatrice_nnps.append(i[0])
    print(FreqDist(beatrice_nnps).most_common(10))

    benedick_tokens = word_tokenize(" ".join(benedick_lines))
    filtered_benedick_tokens = [w for w in benedick_tokens if not w in stop_words and not w in string.punctuation and not w in ["’"]]
    benedick_fdist = FreqDist(filtered_benedick_tokens)
    # print(benedick_fdist.most_common(10))
    # print(len(set(filtered_benedick_tokens))/len(filtered_benedick_tokens))
    benedick_nnps = []
    for i in nltk.pos_tag(filtered_benedick_tokens):
        if i[1]=="NNP":
            benedick_nnps.append(i[0])
    print(FreqDist(benedick_nnps).most_common(10))