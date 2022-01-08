from collections import Counter
from pprint import pprint as pp

class Solution:
    # bucket sort
    # since k is in the range [1, the number of unique elements in the array]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        counts = Counter(nums).items()
        
        # add elements in buckets based on their frequencies
        for ele, freq in counts:
            buckets[freq].append(ele)
        # pp(buckets)
        
        # flatten all lists of elements
        flattened_list = [ele for sublist in buckets for ele in sublist]
        # pp(flattened_list)
        
        return flattened_list[::-1][:k]
        
        
        