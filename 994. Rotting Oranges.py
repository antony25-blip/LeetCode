class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        time=[[float('inf')]*col for _ in range(row)]
        def dfs(i,j,curr_time):
            if i<0 or i>=row or j<0 or j>=col or grid[i][j]==0 or curr_time>=time[i][j]:
                return
            time[i][j]=curr_time
            dfs(i-1,j,curr_time+1)
            dfs(i+1,j,curr_time+1)
            dfs(i,j-1,curr_time+1)
            dfs(i,j+1,curr_time+1)
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    dfs(i,j,0)
        time_req=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    if time[i][j]==float('inf'):
                        return -1
                    time_req=max(time_req,time[i][j])
        return time_req
