from pprint import pprint as pp

class Solution:
    def longestStrChain(self, strings: List[str]) -> int:
        strings.sort(key=len)
        # print(strings)
        stringChains = {string:{"nextStr":"", "maxLen":1} for string in strings}

        for string in strings:
            for idx in range(len(string)):
                curr_str = string[:idx] + string[idx+1:]

                if curr_str in stringChains:
                    old_len = stringChains[string]["maxLen"]
                    new_len = stringChains[curr_str]["maxLen"] + 1

                    if old_len < new_len:
                        stringChains[string]["nextStr"] = curr_str
                        stringChains[string]["maxLen"] = new_len

        # pp(stringChains)
        ans = 0
        for word in stringChains:
            ans = max(ans, stringChains[word]['maxLen'])
            
        return ans

		
		
	