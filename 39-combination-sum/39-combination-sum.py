class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def combiHelper(start_idx, sum_, curr_arr):
            if sum_ == target:
                result.append(curr_arr[:])
                return
            
            for idx in range(start_idx, len(candidates)):
                ele = candidates[idx]
                if sum_ + ele > target:
                    break
                combiHelper(idx, sum_ + ele, curr_arr + [ele])    
                
        combiHelper(0, 0, [])
        return result
                
                
                
                
        