class Solution:
    def kthSmallest(self,arr, l, r, k):
        arr.sort()
        l=arr[:k]
        r=l[-1]
        return r
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
