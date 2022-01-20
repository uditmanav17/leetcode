
class Solution:
    def numTrees(self, n: int) -> int:
        cache = [1]

        for curr_total_nodes in range(1, n + 1):
            trees = 0
            
            for left_nodes in range(curr_total_nodes):
                right_nodes = curr_total_nodes - 1 - left_nodes

                left_tooplogies = cache[left_nodes]
                right_topologies = cache[right_nodes]

                trees += left_tooplogies * right_topologies
                
            cache.append(trees)

        return cache[-1]
