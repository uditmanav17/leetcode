class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace("//", "/")
        path = path.split("/")
        
        ans = []
        
        for p in path:
            if not p or p == ".": 
                continue
            
            if p == "..": 
                if ans: ans.pop()
                continue
                
            ans.append(p)
           
        # print(ans)
        
        return "/" + "/".join(ans)
                
        
        
        
        