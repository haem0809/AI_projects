cleaned_data = open('cleaned_data.txt', mode = 'r', encoding = 'utf-8')
words = cleaned_data.read()
cleaned_data.close()

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

#단어 토큰화
word_tokens = word_tokenize(words)

#원형 복원(Lemmatization)
lemmatizer = WordNetLemmatizer()

nltk_pos_lemmatizing_sentences = []
lemmatizing_sentence = []

for token in pos_tag(word_tokens):
    if token[1] in ["JJ", "JJR", "JJS"]:
        lemma = lemmatizer.lemmatize(token[0], pos="a")
    elif token[1] in ["NN", "NNP", "NNS", "PRP", "PRP$"]:
        lemma = lemmatizer.lemmatize(token[0], pos="n")
    elif token[1] in ["RB", "RBR", "RBS"]:
        lemma = lemmatizer.lemmatize(token[0], pos="r")
    elif token[1] in ["MD", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]:
        lemma = lemmatizer.lemmatize(token[0], pos="v")
    else:
        lemma = lemmatizer.lemmatize(token[0])
    lemmatizing_sentence.append(lemma)
nltk_pos_lemmatizing_sentences.append(lemmatizing_sentence)

result = nltk_pos_lemmatizing_sentences[0]

file_path = "normalized_data.txt" # 파일 저장
with open(file_path, "w") as file:
    for i in result:
        file.write(i + " ")