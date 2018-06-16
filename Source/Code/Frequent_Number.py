import numpy as np

a = np.array([1,3,4,2,3,4,5,6,7,4,3,6,7,3,2])
counts = np.bincount(a)
print("Most frequent item in the list is", np.argmax(counts))