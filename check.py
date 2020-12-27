import glob
import numpy as np
import re
import pickle
from function import calc_tf_weighting,search
np.seterr(divide='ignore', invalid='ignore')

query = '"ronaldo"'
titles, file_names = search(query)
print(titles)

