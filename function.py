import glob
import numpy as np
import re
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

def load_data_in_a_directory(data_path):
    file_paths = glob.glob(data_path)
    lst_contents = []
    ini_lst_contents = []
    for file_path in file_paths:
        f = open(file_path, encoding="utf-8")
        str = f.read()
        ini_lst_contents.append(str)
        words = re.sub(r'[?|$|.|!|<|=|,|\-|\'|\“|\”|)|(]',r' ',str.lower())
        lst_contents.append(words)
    return (lst_contents, file_paths, ini_lst_contents)

def search(query):
    #Khoi tao tf_idf_doc
    contents , paths, ini_contents = load_data_in_a_directory('D:\\Github\\tf_idf\\data\\*.txt')
    vectorizer = TfidfVectorizer()
    countVectorizer = CountVectorizer()
    tfidf = vectorizer.fit_transform(contents)

    requests = [] #Tập từ khóa cứng
    regex = r"([\'\"])((\\\1|.)*?)\1"
    matches = re.finditer(regex, query, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            if groupNum == 2:
                requests.append(match.group(groupNum).lower())
    query = re.sub(r'[?|$|.|!|<|=|,|\-|\'|\“|\”|)|(]',r' ', query.lower())    
    qcontent = query.split()
    #tinh tf_idf_query
    query_vec = vectorizer.transform([query])
    #so sanh bang do do cosin
    results = cosine_similarity(tfidf,query_vec).reshape((-1,))
    rank= results.argsort()[-10:][::-1]
    #print(rank)
    topK = 5
    count = 0
    titles = []
    file_names = []
    for i in range(topK):
        kt = 0
        for request in requests:
            if request in ini_contents[rank[i]].lower():
                kt += 1
        if kt == len(requests):
            count += 1
            #print('file paths', paths[rank[i]][-5])
            file_names.append(paths[rank[i]])
            f = open(paths[rank[i]], encoding="utf-8")
            title = f.readline()
            #print("title",title)
            titles.append(title[:-1])
    return titles, file_names