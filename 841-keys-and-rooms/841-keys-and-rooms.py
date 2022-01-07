
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()
        q = deque([0])
        
        while q:
            curr_node = q.popleft()
            visited.add(curr_node)
            
            for next_node in rooms[curr_node]:
                if next_node not in visited:
                    q.append(next_node)
                    
        return len(rooms) == len(visited)
        