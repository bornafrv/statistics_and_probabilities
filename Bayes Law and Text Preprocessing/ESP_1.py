import hazm as hz
import pandas as pd
import math

punctuations = [',', '.', ')', '(', ':', '«', '،', '»' , '؟' , '،' , '؛' , '-' , 'ـ' , '٪' , '!' , '٬', '<', '>', '{', '}', '[', ']', '?', '|', '#', '/', '^', '\'', '\"']
persian_numbers = {'۱','۲','۳','۴','۵','۶','۷','۸','۹','۰' }
stopwords = hz.stopwords_list()
normalizer = hz.Normalizer()
tokenizer = hz.WordTokenizer()
lemmatizer = hz.Lemmatizer()

df_train = pd.read_csv('books_train.csv')
df_test = pd.read_csv('books_test.csv')

def normalize_text(df):
    for row in range(len(df)):
        df.loc[row]["title"] = normalizer.normalize(df.loc[row]["title"])
        df.loc[row]["description"] = normalizer.normalize(df.loc[row]["description"])
    return df

def remove_puncs_and_nums(df):
    for row in range(len(df)):
        result_title = ""
        result_description = ""
        for char in df.loc[row]["title"]:
            if char not in punctuations and char not in persian_numbers: result_title += char
        df.loc[row]["title"] = result_title
        for char in df.loc[row]["description"]:
            if char not in punctuations and char not in persian_numbers: result_description += char
        df.loc[row]["description"] = result_description
    return df

def tokenize_text(df):
    for row in range(len(df)):
        df.loc[row]["title"] = tokenizer.tokenize(df.loc[row]["title"])
        df.loc[row]["description"] = tokenizer.tokenize(df.loc[row]["description"])
    return df

def lemmatize_text(df):
    for row in range(len(df)):
        result_title = []
        result_description = []
        for index in range(len(df.loc[row]["title"])):
            result_title.append(lemmatizer.lemmatize(df.loc[row]["title"][index]))
        df.loc[row]["title"] = result_title
        for index in range(len(df.loc[row]["description"])):
            result_description.append(lemmatizer.lemmatize(df.loc[row]["description"][index]))
        df.loc[row]["description"] = result_description
    return df

def remove_stopwords(df):
    for row in range(len(df)):
        result_title = []
        result_description = []
        for word in df.loc[row]["title"]:
            if word not in stopwords: result_title.append(word)
        df.loc[row]["title"] = result_title
        for word in df.loc[row]["description"]:
            if word not in stopwords: result_description.append(word)
        df.loc[row]["description"] = result_description        
    return df

def preprocess(df):
    df = normalize_text(df)
    df = remove_puncs_and_nums(df)
    df = tokenize_text(df)
    df = lemmatize_text(df)
    df = remove_stopwords(df)
    return df

def list_words(df):
    words = []
    for row in range(len(df)):
        for word in df.loc[row]["title"]: words.append(word)
        for word in df.loc[row]["description"]: words.append(word)
    return words

def create_bow(df):
    for word in list_of_unique_words: 
        for index in range(len(BoW)): BoW[index][word] = 0.1   #  0
    for row in range(len(df)):
        df_words = []
        if df.loc[row]["categories"] == "مدیریت و کسب و کار":
            df_words += (df.loc[row]["title"] + df.loc[row]["description"])
            for word in df_words:
                BoW[0][word] = BoW[0].get(word) + 1
        elif df.loc[row]["categories"] == "رمان":
            df_words += (df.loc[row]["title"] + df.loc[row]["description"])
            for word in df_words:
                BoW[1][word] = BoW[1].get(word) + 1
        elif df.loc[row]["categories"] == "کلیات اسلام":
            df_words += (df.loc[row]["title"] + df.loc[row]["description"])
            for word in df_words:
                BoW[2][word] = BoW[2].get(word) + 1
        elif df.loc[row]["categories"] == "داستان کودک و نوجوانان":
            df_words += (df.loc[row]["title"] + df.loc[row]["description"])
            for word in df_words:
                BoW[3][word] = BoW[3].get(word) + 1
        elif df.loc[row]["categories"] ==  "جامعه‌شناسی":
            df_words += (df.loc[row]["title"] + df.loc[row]["description"])
            for word in df_words:
                BoW[4][word] = BoW[4].get(word) + 1
        elif df.loc[row]["categories"] ==  "داستان کوتاه":
            df_words += (df.loc[row]["title"] + df.loc[row]["description"])
            for word in df_words:
                BoW[5][word] = BoW[5].get(word) + 1

def sum_of_words_of_cats(bow):
    list_result = []
    for index in range(len(bow)):
        result = 0
        values = bow[index].values()
        for v in values: result += v
        list_result.append(result)
    return list_result

def probability_wordlist_in_cat(bow, words):
    counts_of_cat_words = sum_of_words_of_cats(bow)
    cat = -1
    max_prob = -1000000
    for index in range(len(bow)):
        prob = 0
        for word in words:
            if word in bow[index]:
                result = float(bow[index].get(word)) / float(counts_of_cat_words[index])
                prob += math.log10(result)
                #prob *= result
        if max_prob < prob : 
            max_prob = prob
            cat = index
    if cat == 0: return "مدیریت و کسب و کار"
    elif cat == 1: return "رمان"
    elif cat == 2: return "کلیات اسلام"
    elif cat == 3: return "داستان کودک و نوجوانان"
    elif cat == 4: return "جامعه‌شناسی"
    elif cat == 5: return "داستان کوتاه"
    else: return "none"

def probability_book_category(bow, df):
    for row in range(len(df)):
        cat = probability_wordlist_in_cat(bow, df.loc[row]["description"])
        list_cat.append(cat)

def project_percent_truth(df):
    sum = 0
    for row in range(len(df)):
        if df.loc[row]["categories"] == list_cat[row]: sum += 1
    return sum / 4.5


list_cat = []
df_train = preprocess(df_train)
df_test = preprocess(df_test)
list_of_words_train = list_words(df_train)
list_of_unique_words = list(set(list_of_words_train))
BoW = [{}, {}, {}, {}, {}, {}]
create_bow(df_train)
probability_book_category(BoW, df_test)
percent = project_percent_truth(df_test) 
print(percent)