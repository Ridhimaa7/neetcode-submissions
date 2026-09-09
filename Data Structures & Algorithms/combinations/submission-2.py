class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combList = []
        def backtrack(i,curComb, combList,k):
            if len(curComb) == k:
                combList.append(curComb.copy())
                return
            if i > n:
                return
            for j in range(i,n+1):
                curComb.append(j)
                backtrack(j+1,curComb,combList,k)
                curComb.pop()
        backtrack(1, [], combList, k)
        return combList
        