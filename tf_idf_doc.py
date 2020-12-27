import glob
import numpy as np
import re
import pickle
from function import *
np.seterr(divide='ignore', invalid='ignore')
#chcp 65001

# MAIN

# BUOC 1: Load cac file trong 'data' va xay dụng tap cac tu vung
contents, paths = load_data_in_a_directory('D:\\Github\\truyvan\\data\\*.txt')
with open("contents.txt", "wb") as fp:
    pickle.dump(contents, fp)
with open("paths.txt", "wb") as fp:
    pickle.dump(paths, fp)
vocab = build_dictionary(contents)
vocab =list(vocab)
with open("vocab.txt", "wb") as fp:
    pickle.dump(vocab, fp)

# BUOC 2: Xay dung vector TF weighting cho 
# tap van ban va truy van
TF = calc_tf_weighting(vocab, contents)
# np.save('TF.npy',TF)
with open("TF.txt", "wb") as fp:
    pickle.dump(TF, fp)

query='Ronaldo hét lên mừng bàn thắng của Morata'
#query = input()
print('query: ', query)
requests = []
regex = r"([\'\"])((\\\1|.)*?)\1"
matches = re.finditer(regex, query, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        if groupNum == 2:
            requests.append(match.group(groupNum))
print('Từ khóa cứng: ', requests)
query = query.replace('"', '') 
qcontent = query.split()
qTF = calc_tf_weighting(vocab, [qcontent])
print(qTF.shape)
# BUOC 3: Xay dung vector IDF weight cho tap van ban
DF = np.sum(TF!=0, axis=1)
IDF = 1 + np.log(len(contents) / DF)
IDF = np.array([IDF]).T
# np.save('IDF.npy',IDF)
with open("IDF.txt", "wb") as fp:
    pickle.dump(IDF, fp)


# # BUOC 4: Xay dung vector TF_IDF weighting cho
# # tap van ban va truy van
TF_IDF = TF*IDF
qTF_IDF = qTF*IDF

# BUOC 5: Tinh do tuong dong cua query va cac van ban
# su dung TF_IDF weighting
dists = np.linalg.norm(qTF_IDF - TF_IDF, axis=0)
# BUOC 6: Sap xep de sap hang va hien thi ket qua
rank = np.argsort(dists)
print(rank[:10])
#print(rank)
topK = 2
count = 0
for i in range(topK):
    #print('Van ban gan thu ', i+1, ' la: ', ' '.join(contents[rank[i]]))
    kt = 0
    for request in requests:
        if request in ' '.join(contents[rank[i]]):
            kt += 1
    if kt == len(requests):
        count += 1
        print('file paths', paths[rank[i]])
        f = open(paths[rank[i]], encoding="utf-8")
        line1 = f.readline()
        print('title', line1)
if count == 0:
    print("Không có kết quả nào thỏa")
