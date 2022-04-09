class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        counts = Counter(nums).items()
        
        for ele, freq in counts:
            buckets[freq].append(ele)
            
        flatten_list = [ele for sublist in buckets for ele in sublist]
        # print(flatten_list)
        
        return flatten_list[-k:]
        