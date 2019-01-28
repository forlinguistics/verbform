import nltk

nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer


def getwords(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    tokens = text.split()
    trash = "!.,<>{}[]\"()?/-—"
    good = []
    for i in tokens:
        i = clear_text(i, trash)
        if not i == "":
            good.append(i.lower())
    return good


def clear_text(text, trash):
    text = text.strip(trash)
    return text


words = getwords('text.txt')
past_tense = [i for i in words if i[-2:] == 'ed']
print(len(words))
e_y_count = 0
for word in words:
    #print(word + "-->" + WordNetLemmatizer().lemmatize(word, 'v'))
    if WordNetLemmatizer().lemmatize(word, 'v')[-1:] in ['e', 'y']:
        e_y_count += 1
print(e_y_count)
