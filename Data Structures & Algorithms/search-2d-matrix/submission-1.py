class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)-1
        check = []
        while(l<=r):
            mid = (l+r) // 2
            if(matrix[mid][0] == target):
                return True
            elif(matrix[mid][0]<=target):
                l = mid+1
            else:
                r = mid-1
        check = matrix[r]
        left,right = 0, len(check)-1
        while left <= right:
            m = (left + right) // 2

            if check[m] == target:
                return True
            elif check[m] < target:
                left = m + 1
            else:
                right = m - 1

        return False