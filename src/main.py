import numpy as np

from analytics import analyze

k_range = [1, 3, 5, 7]

filepath = "spambase/spambase.data"

for k in k_range:
    matrix, hit_accurency, fault_accurency = analyze(k, filepath)
    print("k=", k)
    print(np.array(matrix))
    print(hit_accurency)
    print(fault_accurency)
    print()
