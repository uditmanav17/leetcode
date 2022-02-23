
from functools import cmp_to_key

class Solution:
    
    def largestNumber(self, nums: List[int]) -> str:
        def custom_comparator(n1:str, n2:str):
            if n1 + n2 > n2 + n1:
                return 1
            else:
                return -1
    
        str_nums = sorted(map(str, nums), 
                          key=cmp_to_key(custom_comparator), 
                          reverse=True)
        # print(str_nums)
        ans = "".join(str_nums)
        return ans if ans[0] !="0" else "0"
