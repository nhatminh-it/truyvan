import glob
import numpy as np
import re
import pickle


def load_data_in_a_directory(data_path):
    file_paths = glob.glob(data_path)
    lst_contents = []
    for file_path in file_paths:
        f = open(file_path, encoding="utf-8")
        str = f.read()
        words = str.replace('"', '').replace('.', '').replace("'","").split()
        #words = set(words)
        lst_contents.append(words)
    return (lst_contents, file_paths)

# Doc noi dung cua tung file txt
# va xay dung tap "dictionary" chua danh sach cac tu
def build_dictionary(contents):
    dictionary = set()
    for content in contents:
        dictionary.update(content)
    return dictionary

def calc_tf_weighting(vocab, contents):
    TF = np.zeros((len(vocab), len(contents)))
    for i, word in enumerate(vocab):
        for j, content in enumerate(contents):
            TF[i,j] = content.count(word)
    # Chuan hoa
    TF = TF / np.sum(TF, axis=0)
    return TF


def search(query):

    with open(r"D:\Github\truyvan\contents.txt", "rb") as fp: 
        contents = pickle.load(fp)
    with open(r"D:\Github\truyvan\vocab.txt", "rb") as fp: 
        vocab = pickle.load(fp)
    with open(r"D:\Github\truyvan\paths.txt", "rb") as fp: 
        paths = pickle.load(fp)
    with open(r"D:\Github\truyvan\TF.txt", "rb") as fp: 
        TF = pickle.load(fp)  
    with open(r"D:\Github\truyvan\IDF.txt", "rb") as fp: 
        IDF = pickle.load(fp)  
    # TF = np.load(r'D:\Github\truyvan\TF.npy')
    # IDF = np.load(r'D:\Github\truyvan\IDF.npy')

    #query='Ronaldo hét lên mừng bàn thắng của Morata'
    #query = input()
    #print('query: ', query)
    requests = []
    regex = r"([\'\"])((\\\1|.)*?)\1"
    matches = re.finditer(regex, query, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            if groupNum == 2:
                requests.append(match.group(groupNum))
    #print('Từ khóa cứng: ', requests)
    query = query.replace('"', '')
    qcontent = query.split()
    qTF = calc_tf_weighting(vocab, [qcontent])

    # BUOC 4: Xay dung vector TF_IDF weighting cho
    # tap van ban va truy van

    TF_IDF = TF*IDF
    qTF_IDF = qTF*IDF
    # BUOC 5: Tinh do tuong dong cua query va cac van ban
    # su dung TF_IDF weighting
    dists = np.linalg.norm(qTF_IDF - TF_IDF, axis=0)
    # BUOC 6: Sap xep de sap hang va hien thi ket qua
    rank = np.argsort(dists)
    #print(rank)
    topK = 5
    count = 0
    titles = []
    file_names = []
    for i in range(topK):
        #print('Van ban gan thu ', i+1, ' la: ', ' '.join(contents[rank[i]]))
        kt = 0
        for request in requests:
            if request in ' '.join(contents[rank[i]]).lower():
                kt += 1
        if kt == len(requests):
            count += 1
            #print('file paths', paths[rank[i]][-5])
            file_names.append(paths[rank[i]][-5:])
            f = open(paths[rank[i]], encoding="utf-8")
            title = f.readline()
            #print("title",title)
            titles.append(title[:-1])
    # if count == 0:
    #     print("Không có kết quả nào thỏa")
    return titles, file_names