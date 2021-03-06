from typing import List

class Solution:
    def simplifyPath(self, path: str) -> str:
        #
        for c in path:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, len(nums)
        mid = 1 # value of the middle elements
        while j < k: 
            if nums[j] < mid:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > mid:
                k -= 1
                nums[j], nums[k] = nums[k], nums[j]
            else:
                j += 1
            
            