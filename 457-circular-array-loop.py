class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def dfs(node, step):
            next_node = (node + step) % len(nums)
            next_step = nums[next_node]
            if visited[next_node]: #cycle
                return True
            if next_step * step < 0 or next_node == node: #different way or 1-element-cycle
                return False
            visited[node]=True
            return dfs(next_node,next_step)    

        
        for idx, step in enumerate(nums):
            visited = [False for i in range(len(nums))]
            if dfs(idx, step):
                return True
        return False