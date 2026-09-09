class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combList = []
        def backtrack(i,curComb, combList,k):
            if len(curComb) == k:
                combList.append(curComb.copy())
                return
            if i > n:
                return
            curComb.append(i)
            backtrack(i+1,curComb,combList,k)
            curComb.pop()
            backtrack(i+1,curComb,combList,k)
            #return combList
        backtrack(1,[],combList,k)
        return combList
        