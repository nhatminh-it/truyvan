import glob
import numpy as np
import re
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_selection import SelectKBest, chi2

def remove_stopword(query):
  stop_word = ['bị', 'bởi', 'cả', 'các', 'cái', 'cần', 'càng', 'chỉ',
               'chiếc', 'cho', 'chứ', 'chưa', 'chuyện', 'có', 'có_thể', 'cứ', 'của', 'cùng', 'cũng', 'đã', 
               'đang', 'đây', 'để', 'đến_nỗi', 'đều', 'điều', 'do', 'đó', 'được', 'dưới', 'gì', 'khi', 'không', 'là',
               'lại', 'lên', 'lúc', 'mà', 'mỗi', 'một_cách', 'này', 'nên', 'nếu', 'ngay', 'nhiều', 'như', 'nhưng', 'những',
               'nơi', 'nữa', 'phải', 'qua', 'ra', 'rằng', 'rằng', 'rất', 'rất', 'rồi', 'sau', 'sẽ', 'so', 'sự', 'tại', 'theo',
               'thì', 'trên', 'trước', 'từ', 'từng', 'và', 'vẫn', 'vào', 'vậy', 'vì', 'việc', 'với', 'vừa']
  result = []             
  for word in query.split():
    if word not in stop_word:
      result.append(word)
  return ' '.join(result)

def load_data_in_a_directory(data_path):
    file_paths = glob.glob(data_path)
    lst_contents = []
    ini_lst_contents = []
    for file_path in file_paths:
        f = open(file_path, encoding="utf-8")
        str = f.read()
        ini_lst_contents.append(str)
        words = re.sub(r'[?|$|.|!|<|=|,|\-|\'|\“|\”|)|(]',r' ',str.lower())
        words = remove_stopword(words)
        lst_contents.append(words)
    return (lst_contents, file_paths, ini_lst_contents)

def search(query):
    # Load data
    with open ('contents', 'rb') as fp:
        contents = pickle.load(fp)
    with open ('paths', 'rb') as fp:
        paths = pickle.load(fp)
    with open ('ini_contents', 'rb') as fp:
        ini_contents= pickle.load(fp)
    # Khởi tạo tf_idf vecter cho docs
    vectorizer = TfidfVectorizer(max_features = 10000)
    tfidf = vectorizer.fit_transform(contents)
    # Khởi tạo tập từ khóa cứng (nếu có)
    requests = [] # Tập từ khóa cứng
    regex = r"([\'\"])((\\\1|.)*?)\1"
    matches = re.finditer(regex, query, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            if groupNum == 2:
                requests.append(match.group(groupNum).lower())
    query = re.sub(r'[?|$|.|!|<|=|,|\-|\'|\“|\”|)|(]',r' ', query.lower())    
    query = remove_stopword(query)
    qcontent = query.split()
    # Tính tf_idf_query
    query_vec = vectorizer.transform([query])
    # So sánh kết quả bằng độ do cosin
    results = cosine_similarity(tfidf,query_vec).reshape((-1,))
    rank= results.argsort()[-20:][::-1]
    #print(rank)
    topK = 10
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
    try:
        file_names = file_names[:5]
        titles = titles[:5]
    except:
        pass
    return titles, file_names