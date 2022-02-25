class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split(".")]
        
        # print(v1, v2)
        
        for i in range(max(len(v1), len(v2))):
            v1_sub = v1[i] if i < len(v1) else 0
            v2_sub = v2[i] if i < len(v2) else 0
            
            if v1_sub < v2_sub:
                return -1
            elif v1_sub > v2_sub:
                return 1
                        
        return 0
        