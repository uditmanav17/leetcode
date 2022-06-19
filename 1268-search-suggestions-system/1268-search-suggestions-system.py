class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        arr = sorted(products)
        ans = []
        l, r = 0, len(products) - 1
        
        for idx, prefix in enumerate(searchWord):
            prefix = searchWord[:idx+1]
            temp_arr = []
            while arr:
                curr_word = arr.pop(0)
                if curr_word.startswith(prefix):
                    temp_arr.append(curr_word)
            temp_arr, arr = arr, temp_arr
            ans.append(arr[:3])
        return ans
                
        