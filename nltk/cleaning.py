diary_in = open('raw_data.txt', mode = 'r', encoding = 'utf-8')
diary = diary_in.read()
diary_in.close()

import nltk
from nltk.corpus import stopwords
import re
from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker

#1. 텍스트 클리닝(문장부호 제거)
def cleaning(text):
    pattern = '([a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+)' # E-mail제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '(http|ftp|https)://(?:[-\w.]|(?:%[\da-fA-F]{2}))+' # URL제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)'  # 한글 자음, 모음 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '<[^>]>'         # HTML 태그 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '[^\w\s\n]'         # 특수기호제거
    text = re.sub(pattern=pattern, repl='', string=text)
    return text
diary = cleaning(diary)
shortword = re.compile(r'\W*\b\w{1,2}\b')
shortword = shortword.sub('', diary)

#2. 소문자로 변경
diary = diary.lower()


#3. nltk 불용어 제거 + 단어 토큰화
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(diary)

result = []
for word in word_tokens: 
    if word not in stop_words: 
        result.append(word)


#4. Spellchecker 철자 오류 교정
spell = SpellChecker()

corrected_words = []
for word in result:
    corrected_word =spell.correction(word)
    corrected_words.append(corrected_word)

print(corrected_words)

corrected_words_string = ' '.join(corrected_words)

#5. 텍스트 파일로 저장
with open('cleaned_data.txt', 'w', encoding='utf-8')as file:
    file.write(corrected_words_string)
