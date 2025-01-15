class Solution:
    def majority_element(self, nums: list[int]) -> int:
        candidate = count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate


class BruteForceSolution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        for num in nums:
            count = sum(1 for i in nums if i == num)
            if count > n // 2:
                return num


boyer_moore = Solution()
brute_force = BruteForceSolution()
nums = [1, 4, 1, 4, 4, 3, 3, 4, 2, 4, 4, 2, 4, 4]
print(boyer_moore.majority_element(nums))
print(brute_force.majorityElement(nums))
