from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for edge in prerequisites:
            adj[edge[1]].append(edge[0])
            indegree[edge[0]] += 1

        q = deque()
        res = []
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            top = q.popleft()
            res.append(top)
            for neigh in adj[top]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        
        if len(res) == numCourses:
            return res
        return []


        