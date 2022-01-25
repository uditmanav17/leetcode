class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False 
        
        max_ele_idx = 0
        max_ele = arr[max_ele_idx]
        
        for idx, ele in enumerate(arr):
            if ele > max_ele:
                max_ele_idx = idx
                max_ele = ele
        
        if max_ele_idx == 0 or max_ele_idx == len(arr)-1:
            return False
        
        left_idx = max_ele_idx
        while left_idx > 0:
            curr_ele = arr[left_idx]
            left_idx -= 1
            prev_left_ele = arr[left_idx]
            if curr_ele <= prev_left_ele:
                # print("left")
                return False
            
        right_idx = max_ele_idx
        while right_idx < (len(arr)-1):
            curr_ele = arr[right_idx]
            right_idx += 1
            prev_right_ele = arr[right_idx]
            if curr_ele <= prev_right_ele:
                # print("right - ", curr_ele, prev_right_ele)
                return False
        
        return True
