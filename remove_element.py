class Solution:
    def remove_element(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


rand_num = [0, 1, 0, 0, 3, 0, 4, 0]
k = 0
soln = Solution()
result = soln.remove_element(rand_num, k)
print(result)
