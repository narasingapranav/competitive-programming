import numpy as np

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        N = len(queries[0])
        q_vec = np.array([[ord(c) for c in w] for w in queries], dtype=np.int8)
        d_vec = np.array([[ord(c) for c in w] for w in dictionary], dtype=np.int8)
        results = []
        for i in range(len(queries)):
            diff = q_vec[i] != d_vec
            edit_counts = np.sum(diff, axis=1)
            if np.any(edit_counts <= 2):
                results.append(queries[i])
                
        return results        