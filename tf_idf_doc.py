from function import *


contents , paths, ini_contents = load_data_in_a_directory('D:\\Github\\tf_idf\\data\\*.txt')
with open('contents', 'wb') as fp:
    pickle.dump(contents, fp)
with open('paths', 'wb') as fp:
    pickle.dump(paths, fp)
with open('ini_contents', 'wb') as fp:
    pickle.dump(ini_contents, fp)
