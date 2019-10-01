class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l=0
        r=len(A)-1
        while l<r:
            while l<r and A[l]%2==0 :
                l+=1
            while r>=l and A[r]%2!=0 :
                r-=1
            if(l<r):
                A[r], A[l] = A[l], A[r]
                l+=1
                r-=1
        return A