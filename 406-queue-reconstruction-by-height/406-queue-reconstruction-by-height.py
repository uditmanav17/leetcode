class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        people.sort(key=lambda x: (x[0], -x[1]))
        ans = [None]*len(people)
        idx = list(range(len(people)))
        
        for p in people:
            ans[idx.pop(p[1])] = p
        return ans
