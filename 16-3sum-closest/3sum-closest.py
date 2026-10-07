class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        result = 0
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1
            while left< right:
                currentSum = nums[i] + nums[left] + nums[right]
                if ans > abs(currentSum - target):
                    result = currentSum
                    ans = abs(currentSum - target)
                if currentSum < target:
                    left += 1
                elif currentSum > target:
                    right -= 1
                else:
                    return result
        return result 

