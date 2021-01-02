class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result, path = [], []
        if k <= 0 or n < k:
            return result
        self.dfs(n, k, 1, path, result)
        return result

    def dfs(self, n, k, begin, path, result: List[int]):
        if len(path) == k:
            result.append(path[:])
            return

        for i in range(begin, n + 1):
            path.append(i)
            self.dfs(n, k, i + 1, path, result)
            path.pop()
